from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

driver = webdriver.Chrome("/usr/bin/chromedriver_linux64/chromedriver")

driver.get('https://worker.mturk.com/projects?ref=w_pl_prvw')

title=[]
value=[]
description=[]

content=driver.page_source
soup=BeautifulSoup(content, 'html.parser')

for a in soup.findAll('div', attrs={'class':'desktop-row hidden-sm-down', 'class':'p-b-sm col-xs-12 col-md-6'}):
    name=a.find('span', attrs={'class':'p-x-sm column text-truncate project-name-column hidden-sm-down'})
    price=a.find('span', attrs={'class':'p-x-sm column reward-column hidden-sm-down text-xs-right'})
    about=a.find('div', attrs={'class':'p-b-md col-xs-12 col-md-6'})
    title.append(name.text)
    value.append(price.text)
    description.append(about.text)


df=pd.DataFrame({'title': title, 'value': value, 'description': description})
df.to_csv('mturk.csv', index=False, encoding='utf-8')