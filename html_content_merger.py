from angel_urls import *
import os
import shutil


def FindMaxLength(lst):
    maxLength = max(len(x) for x in lst)
    return  maxLength

def merge_scrapped_data(text,angel_number):
    data = ''
    url_wise_content = text.split(page_wise_delimeter)[:-1]
    merger = []
    url_site = []
    for url_content in url_wise_content:
        para_wise_content = url_content.split(para_wise_delim)[:-1]
        page_url = url_content.split(para_wise_delim)[-1]
        url_site.append(page_url[page_url.find('http'):])
        merger.append(para_wise_content)
    maxLength = FindMaxLength(merger)
    for i in range(maxLength):
        for j in range(len(merger)):
            if len(merger[j]) > 0:
                temp_data =  merger[j][0]
                merger[j].remove(temp_data)
                data = data + '<a href = ' +  url_site[j] + '>' + url_site[j] + '</a><br>' + temp_data
            else:
                data = data + '<a href = ' + url_site[j] + '>' + url_site[j] + '</a><br>'
    with open('Angel_number_html/' + str(angel_number) + '.html', 'w') as f:
        f.write(data)
    shutil.copyfile('Angel_number_html/' + str(angel_number) + '.html', 'Angel_number_txt/' + str(angel_number) + '.txt')




