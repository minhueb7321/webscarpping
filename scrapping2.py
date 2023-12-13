import pandas as pd
from bs4 import BeautifulSoup
import html5lib
import requests
import csv
import warnings
import openpyxl
warnings.filterwarnings('ignore')
pd.set_option('display.max_rows' , 100)
pd.set_option('display.max_columns' , 10)
#s
headers = {'User-Agent' : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246"}
URL = "http://www.values.com/inspirational-quotes"
request = requests.get(URL, headers = headers)
soup = BeautifulSoup(request.content, 'html.parser')
dataframe = pd.DataFrame(columns = ['theme', 'url', 'img', 'lines', 'author'] , dtype='str')
quotes = [] # a list to store quotes
table = soup.find('div', attrs = {"id" : "all_quotes"})
#print(table)
for row in table.findAll('div', attrs = {"class":"col-6 col-lg-4 text-center margin-30px-bottom sm-margin-30px-top"}):
    quote = {}
    # theme => h5 tag => h5.text
    quote['theme'] = row.h5.text
    # url => a - href = True => a['href']
    quote['url'] = row.a['href']
    # img => img tag => img['src']
    quote['img'] = row.img['src']
    # lines => img['alt'] . split ("#")[0] => quotes -main
    quote['lines'] = row.img['alt'].split(" #")[0]
    # author => img['alt'] . split ("#")[1]=> author 
    quote['authors'] = row.img['alt'].split(" #")[1]
    quotes.append(quote)
print(quotes)
print("*" * 40)
print(len(quotes))
print("*" * 40)
for i in quotes :
    print(i.get('theme', None)) 
print("*" * 40)
for i in quotes :
    print(i.keys())
theme_list =  []
url_list = []
img_list = []
lines_list = []
author_list = []
for sub_dict in quotes:
    #for sub_dict in sub_list :
    theme_ = sub_dict.get('theme', None)
    theme_list.append(theme_)
    url_ =  sub_dict.get('url', None)
    url_list.append(url_)
    img_ = sub_dict.get('img', None)
    img_list.append(img_)
    lines_ = sub_dict.get('lines', None)
    lines_list.append(lines_)
    author_ = sub_dict.get('authors', None)
    author_list.append(author_)
dataframe['theme'] = theme_list
dataframe['url'] = url_list
dataframe['img'] = img_list
dataframe['lines'] = lines_list
dataframe['author'] = author_list
print("*" * 40)
print(dataframe.head(5))
print("*" * 40)
print(dataframe.info())
print("*" * 40)
print(dataframe.describe(include = "all"))
dataframe.to_excel(r'F:\Git\webscarpping\scrapping.xlsx', index =False)