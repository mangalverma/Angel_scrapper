import pandas as pd
import os
from urllib.parse import urlparse

if not os.path.exists('../UpWork-project-Mangal/interested_urls'):
	os.mkdir('../UpWork-project-Mangal/interested_urls')

if not os.path.exists('../UpWork-project-Mangal/non_interested_urls'):
	os.mkdir('../UpWork-project-Mangal/non_interested_urls')

if not os.path.exists('../UpWork-project-Mangal/doubtful_urls'):
    os.mkdir('../UpWork-project-Mangal/doubtful_urls')

if not os.path.exists('../UpWork-project-Mangal/xml_files'):
    os.mkdir('../UpWork-project-Mangal/xml_files')

os.chdir("../UpWork-project-Mangal/unverified_urls")

for filename in os.listdir(os.getcwd()):
    interested_urls = []
    doubtful_urls = []
    non_interested_urls = []
    xml_files = []
    data = pd.read_csv(filename)
    urls = data.iloc[:,0].tolist()
    for url in urls:
        parsed_url = urlparse(url)
        url_without_query_string = parsed_url.scheme + "://" + parsed_url.netloc + parsed_url.path
        extension = url_without_query_string[url_without_query_string.rfind('.')+1:]
        if url_without_query_string == "https://divineangelnumbers.com/wp-content/uploads/2021/08/Footprints-In-The-Sand.pdf":
            print("k")
        ignore_extensions = ['php', 'png', 'jpg', 'pdf']
        if extension not in ignore_extensions:
            if "xml" in extension:
                xml_files.append(url)
            else:
                if "number" in url_without_query_string and   any(char.isdigit() for char in url_without_query_string):
                    if "@msn.com" in url_without_query_string:
                        url_without_query_string = url_without_query_string[:url_without_query_string.rfind('/')]
                    if "angel" in url_without_query_string and url_without_query_string.split('/')[-2] != 'page':
                        interested_urls.append(url_without_query_string)
                    else:
                        doubtful_urls.append(url_without_query_string)
                else:
                    non_interested_urls.append(url)

    df = pd.DataFrame({'address':interested_urls})
    df1 = pd.DataFrame({'address':doubtful_urls})
    df2 = pd.DataFrame({'address':non_interested_urls})
    df3 = pd.DataFrame({'address': xml_files})

    new_filename = filename[filename.find('_')+1:filename.find('.')]
    df.to_csv("../interested_urls/" + new_filename + ".csv",index =True)
    df1.to_csv("../doubtful_urls/" + new_filename + ".csv", index=True)
    df2.to_csv("../non_interested_urls/" + new_filename + ".csv", index=True)
    df3.to_csv("../xml_files/" + new_filename + ".csv", index=True)


    print(filename)