from angel_urls import *
import os
import shutil


def FindMaxLength(lst):
    maxLength = max(len(x) for x in lst)
    return  maxLength

def merge_scrapped_data(text,angel_number):
    url_wise_content = text.split(page_wise_delimeter)
    merger = []
    for url_content in url_wise_content:
        merger.append(url_content.split(para_wise_delim))
    maxLength = FindMaxLength(merger)
    for i in range(maxLength):
        for j in range(len(merger)):
            if len(merger[j][0]) > 0:
                data = merger[j][0]
                merger[j].remove(data)
                with open('Angel_number_html/' + str(angel_number) + '.html', 'a') as f:
                    f.write(data)
    shutil.copyfile('Angel_number_html/' + str(angel_number) + '.html', 'Angel_number_txt/' + str(angel_number) + '.txt')




