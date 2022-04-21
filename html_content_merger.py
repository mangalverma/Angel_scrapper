from angel_urls import *
import os
import shutil
from random import shuffle
from bs4 import BeautifulSoup
import html2text


def FindMaxLength(lst):
    maxLength = max(len(x) for x in lst)
    return  maxLength

def merge_scrapped_data(text,angel_number):
    data = ''
    url_wise_content = text.split(page_wise_delimeter)[:-1]
    shuffle(url_wise_content)
    merger = []
    url_site = []
    for url_content in url_wise_content:
        para_wise_content = url_content.split(para_wise_delim)
        page_url = url_content.split(para_wise_delim)[-1]
        url_site.append(page_url[page_url.find('http'):])
        merger.append(para_wise_content)
    maxLength = FindMaxLength(merger)
    for i in range(maxLength):
        for j in range(len(merger)):
            if len(merger[j]) > 0:
                temp_data =  merger[j][0]
                merger[j].remove(temp_data)
                data = data +  temp_data
    soup = BeautifulSoup(data, "html.parser")
    with open('Angel_number_html/' + str(angel_number) + '.html', 'w') as f:

        data=soup.prettify()
        f.write(data)
    with open('Angel_number_txt/' + str(angel_number) + '.txt', 'w') as f:
        h = html2text.HTML2Text()
        h.ignore_links = True
        for line in h.handle(str(soup)):  # handle() Function only accepts string as parameter
            f.write(line)


