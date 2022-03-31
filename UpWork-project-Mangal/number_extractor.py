import pandas as pd

df = pd.read_csv('interested_urls/sacredscribesangelnumbers.csv')

df['angel_number'] = [url[url.rfind('-')+1: url.rfind('.')] for url in df['address']]

df.to_csv("../manual_csv/sacredscribesangelnumbers.csv",index=False)