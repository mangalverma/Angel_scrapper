from angel_urls import para_wise_delim,page_xpath,remove_attribute,page_wise_delimeter,url_patterns,ignore_site_num,remove_code
import requests
from html.parser import HTMLParser
from lxml import etree
from unicodedata import  normalize
import os
from functools import partial
from html_content_merger import *
from urllib. parse import urlparse
import pandas as pd
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry
from concurrent.futures import ProcessPoolExecutor
import time

UA = 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'

def get_xpath(url):
    for domain_name,xpath in page_xpath:
        if url.startswith(domain_name):
            return xpath
    else:
        print(f'WARNING:add page_xpath for {url}')
        return '//body'

def store_scrapped_data(data,angel_number):
    file_name = f"angel_number-{angel_number}.html"
    with open (file_name,'w') as f:
        f.write(data)
        print(f'Raw data Created for angel number - {angel_number}')


def remove_html_data(url,html_data):
    for domain_name,rplc_code in remove_code.items():
        if url.startswith(domain_name):
            for code in rplc_code:
               print(repr(html_data))
               html_data = html_data.replace(code['orig'],code['new'])
    return html_data

def scrape_and_parse_data(url_patterns,angel_number):

    scrapped_data = ''
    for site_num,patterns in url_patterns.items():
       if int(site_num) not in ignore_site_num:
         for pattern in patterns:
             if '@#$' not in pattern:
                 manual_csv_df = pd.read_csv('manual_csv/'+ pattern)
                 url_series = manual_csv_df.loc[manual_csv_df['angel_number'] == angel_number, 'address']
                 if not url_series.empty:
                     url = url_series.iloc[0]
                 else:
                     print(pattern + ' did not contain angel number ' + str(angel_number))
                     continue
             else:
                url = pattern.replace('@#$', str(angel_number))
             session = requests.Session()
             retry = Retry(connect=3, backoff_factor=0.5)
             adapter = HTTPAdapter(max_retries=retry)
             session.mount('http://', adapter)
             session.mount('https://', adapter)
             response = session.get(url,headers={"User-Agent": UA})
             if response.status_code !=200:
                 print(f"{url} NOT FOUND -{ response.status_code}")
                 continue
             else:
                 if response.url!= url:
                     print(f'url redirect to {response.url}')
                     domain = urlparse(url).netloc
                     redirected_angel_no = response.url[response.url.rfind(url[-2])+1:response.url.rfind(url[-2])+2]
                     try:
                         if response.url == default_redirected.get(domain) or redirected_angel_no.isdigit():
                             print(f"skipping {url} because it is redirecting to homepage/wrong urls {response.url}")
                             continue
                     except:
                         print(f"skipping {url} because it is redirecting to homepage/wrong urls {response.url}")
                         continue
                     url =response.url
                 xpath = get_xpath(url)
                 tree = etree.HTML(response.content)
                 encoded_data = tree.xpath(xpath)
                 html_data = None
                 data_list = []
                 for data in encoded_data:
                   data_list.append(etree.tostring(data).decode('utf-8'))
                 html_data = ''.join(data_list)
                 html_data=remove_html_data(url,html_data)
                 if response.status_code == 200:
                     parser = MYhtmlparser(url)
                     parser.feed(html_data)
                     temp_data = parser.document_content
                     temp_data = remove_html_data(url, temp_data)
                     temp_data+= url+' site'+ site_num+ page_wise_delimeter
                     scrapped_data += temp_data
                     print(f'[{url}]-->Raw data added for angel number - {angel_number}')
                 break
    if scrapped_data:
         merge_scrapped_data(scrapped_data,angel_number)
         store_scrapped_data(scrapped_data,angel_number)

def check_if_ignore_tag_by_domain(tag,url):
    for domain,tags in ignore_tag_by_domain.items():
        if url.startswith(domain) and tag in tags:
           return True
    return False

class MYhtmlparser(HTMLParser):
    document_content = ''
    p_open = False
    is_consecutive_h = False
    ignore_content = False
    current_tag_to_remove = None
    count_removing_tag = 0

    def __init__(self,url):
        self.url = url
        super(MYhtmlparser, self).__init__()



    def is_remove_element(self,tag,attrs,url):
        ignorable_tags = ['script','style','img','noscript']
        if self.ignore_content and tag == self.current_tag_to_remove:
                self.count_removing_tag += 1
        if not self.ignore_content :
            for attr,value in attrs:
                for domain,values in remove_attribute.items():
                    if url.startswith(domain):
                        for attr1,value1 in values.items():
                            if attr == attr1 and (value in value1):
                                self.current_tag_to_remove=tag
                                self.count_removing_tag=1
                                self.ignore_content = True
                                return
            if tag in ignorable_tags or check_if_ignore_tag_by_domain(tag,self.url):
                self.current_tag_to_remove = tag
                self.count_removing_tag += 1
                self.ignore_content = True

    def reset_removing_tag(self,tag):
            if tag == self.current_tag_to_remove:
                self.count_removing_tag -=1
                if self.count_removing_tag==0:
                    self.ignore_content = False
                    self.current_tag_to_remove = None


    def handle_starttag(self, tag, attrs):

        self.is_remove_element(tag, attrs,self.url)
        if not self.ignore_content:
            if tag in ['h1','h2','h3','h4','h5','h6'] :
                if self.is_consecutive_h:
                    self.document_content+=para_wise_delim
                self.document_content += f"<{tag}>"


            if tag == 'p' :
                self.is_consecutive_h = False
                self.document_content += f"<{tag}>"


    def handle_endtag(self,tag):
        if not self.ignore_content:
            if tag in ['h1','h2','h3','h4','h5','h6'] :
                self.document_content += f"</{tag}>"
                self.is_consecutive_h = True
            if tag == 'p':
                self.document_content += f"</{tag}>"
                self.document_content+=para_wise_delim
        self.reset_removing_tag(tag)

    def handle_data(self,data):
        if not self.ignore_content:
            data = data.replace('\n','')
            if data:
                data = normalize("NFKD", data)
                data = data.replace('â€“','-')
                self.document_content+=data

def main():
    t = time.time()
    if not os.path.exists('Angel_number_html'):
        os.mkdir('Angel_number_html')

    if not os.path.exists('Angel_number_txt'):
      os.mkdir('Angel_number_txt')
    func = partial(scrape_and_parse_data, url_patterns)
    with ProcessPoolExecutor() as executor:

        angel_args = (i for i in range(0,5))
        executor.map(func,angel_args)
    t_end=time.time()-t
    print(f"{t_end//60} minutes {t_end%60} seconds")






#ipublishing, mindfuljustice
if __name__ == '__main__':
   main()


#ipublishing, mindfuljustice