import requests 
import pandas as pd
from bs4 import BeautifulSoup   

URL = "https://news.ycombinator.com/"

# get page 
response = requests.get(URL)
if response.status_code != 200:
    raise Exception(f'Failed to load page {URL}')

# parse HTML
sp = BeautifulSoup(response.text, "html.parser")

titles = []
links = []

articles = sp.find_all("tr", class_="athing")

# extract titles, links
for article in articles: 
    titleline = article.find("span", class_="titleline")
    if titleline: 
        a_tag = titleline.find("a")
        titles.append(a_tag.get_text())
        links.append(a_tag['href'])

# add to dataframe 
data = pd.DataFrame({"Title": titles, "Link": links})

# save as CSV 
data.to_csv('h_news.csv', index=False)

print('scrape completed')

