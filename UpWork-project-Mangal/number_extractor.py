import pandas as pd

df = pd.read_csv('interested_urls/numerologynation.csv')

df['angel_number'] = [url[url.rfind('-')+1: url.rfind('/')] for url in df['address']]

df.to_csv("../manual_csv/numerologynation.csv",index=False)