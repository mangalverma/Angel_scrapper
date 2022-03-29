from angel_urls import para_wise_delim,page_xpath,remove_attribute,page_wise_delimeter,url_patterns,ignore_site_num,remove_code
import requests
from html.parser import HTMLParser
from lxml import etree
from unicodedata import  normalize
import os
from html_content_merger import *

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
    for domain_name,rmv_code in remove_code.items():
        if url.startswith(domain_name):
            for code in rmv_code:
               html_data = html_data.replace(code,'')
    return html_data

def scrape_and_parse_data(url_patterns,angel_number):

    scrapped_data = ''
    for site_num,patterns in url_patterns.items():
       if int(site_num) not in ignore_site_num:
         for pattern in patterns:
             url = pattern.replace('@#$', str(angel_number))
             response = requests.get(url,headers={"User-Agent": ""})
             if response.status_code !=200:
                 print(f"{url} NOT FOUND -{ response.status_code}")
                 continue
             else:
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
                     parser = MYhtmlparser()
                     parser.feed(html_data)
                     temp_data = parser.document_content
                     temp_data+= page_wise_delimeter
                     scrapped_data += temp_data
                     print(f'[{url}]-->Raw data added for angel number - {angel_number}')
                 break
    if scrapped_data:
         merge_scrapped_data(scrapped_data,angel_number)



class MYhtmlparser(HTMLParser):

    document_content = ''
    p_open = False
    is_consecutive_h = False
    ignore_content = False
    current_tag_to_remove = None
    count_removing_tag = 0

    def is_remove_element(self,tag,attrs):

        if self.ignore_content and tag == self.current_tag_to_remove:
                self.count_removing_tag += 1
        if not self.ignore_content :
            for attr,value in attrs:
                for attr1,value1 in remove_attribute:
                    if attr == attr1 and (value in value1):
                        self.current_tag_to_remove=tag
                        self.count_removing_tag=1
                        self.ignore_content = True
                        return
            if tag == 'script' :
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

        self.is_remove_element(tag, attrs)
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

if not os.path.exists('Angel_number_html'):
    os.mkdir('Angel_number_html')

if not os.path.exists('Angel_number_txt'):
  os.mkdir('Angel_number_txt')
scrape_and_parse_data(url_patterns,1111)