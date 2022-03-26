from angel_urls import standard_urls,non_standard_urls,page_xpath,remove_attribute
import requests
from html.parser import HTMLParser
from lxml import etree
from unicodedata import  normalize

def get_xpath(url):
    for domain_name,xpath in page_xpath:
        if url.startswith(domain_name):
            return xpath
    else:
        print(f'WARNING:add page_xpath for {url}')
        return '//body'

def scrape_and_parse_data(standard_urls):
    for url in standard_urls:
         url = url.replace('@#$', '55')
         xpath = get_xpath(url)
         response = requests.get(url)
         tree = etree.HTML(response.content)
         data = tree.xpath(xpath)
         data = etree.tostring(data[0]).decode('utf-8')
         if response.status_code == 200:
             parser = MYhtmlparser()
             parser.feed(data)
             with open('angel_55.html','w') as f:
                 f.write(parser.document_content)


class MYhtmlparser(HTMLParser):

    document_content = ''
    p_open = False
    h_open = False
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
                self.document_content += f"<{tag}>"
            if tag == 'p' :
                self.document_content += f"<{tag}>"


    def handle_endtag(self,tag):
        if not self.ignore_content:
            if tag in ['h1','h2','h3','h4','h5','h6'] :
                self.document_content += f"</{tag}>"
            if tag == 'p':
                self.document_content += f"</{tag}>"
        self.reset_removing_tag(tag)

    def handle_data(self,data):
        if not self.ignore_content:
            data = data.replace('\n','')
            if data:
                data = normalize("NFKD", data)
                data = data.replace('â€“','-')
                self.document_content+=data

scrape_and_parse_data(standard_urls)