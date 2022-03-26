from angel_urls import standard_urls,non_standard_urls,xpaths
import requests
from html.parser import HTMLParser
from lxml import etree



def remove_by_xpath(htmlstring):
    tree = etree.HTML(htmlstring)
    element = tree.xpath(xpaths)
    content = etree.tostring(element[0])
    if content in htmlstring:
      htmlstring.replace(content,'')
    else:
        print('not found')


def scrape_and_parse_data(standard_urls):
    for url in standard_urls:
         url = url.replace('@#$', '55')
         response = requests.get(url)

         if response.status_code == 200:
             parser = MYhtmlparser()
             parser.feed(response.text)
             remove_by_xpath(response.text)
             with open('angel_55.html','a') as f:
                 f.write(parser.document_content)


class MYhtmlparser(HTMLParser):
    document_content = ''
    h_open = False
    ignore_content = False
    ignore_tags = ['script','blockquote']
    def handle_starttag(self, tag, attrs):
        if tag in self.ignore_tags :
            self.ignore_content = True
        if not self.ignore_content:
            if tag in ['h1','h2','h3','h4','h5','h6']  :
                self.h_open = True
                self.document_content += f"<{tag}>"
            if tag == 'p' :
                self.document_content += f"<{tag}>"

    def handle_endtag(self,tag):
        if tag in self.ignore_tags :
            self.ignore_content = False
        if tag in ['h1','h2','h3','h4','h5','h6'] :
            self.h_open = False
            self.document_content += f"</{tag}>"


    def handle_data(self,data):
        if not self.ignore_content:
            if data  :
                data = data.replace('â€“','-')
                self.document_content+=data

scrape_and_parse_data(standard_urls)