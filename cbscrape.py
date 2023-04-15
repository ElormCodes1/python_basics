from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd

#1. import necessary libraries, selenium-webdriver: for web testing(automating browser activities),
#  bs4-beautifulsoup: for parsing html, pandas: for data manipulation
#2. create a webdriver object, pass the path of the chromedriver as an argument
#3. get the url of the website you want to scrape
#4. use the webdriver object to get the url
#5. use the webdriver object to get the page source
#6. create a BeautifulSoup object, pass the page source and the parser as arguments
#7. use the BeautifulSoup object to find all the table rows
#8. create an empty list
#9. loop through all the table rows
#10. create an empty dictionary
#11. use the BeautifulSoup object to find all the table data in each row
#12. loop through all the table data
#13. use the BeautifulSoup object to get the text of each table data
#14. append the text to the dictionary
#15. append the dictionary to the list
#16. create a dataframe from the list
#17. print the dataframe
companyname=[]
# location=[]
# reviewcount=[]
# services=[]
# websites=[]


driver = webdriver.Chrome("/usr/bin/chromedriver_linux64/chromedriver")

driver.get("https://www.yelp.com/search?find_desc=Massage&find_loc=San%20Francisco%2C%20CA")

content = driver.page_source
soup = BeautifulSoup(content, 'html.parser')
for a in soup.findAll('a', attrs={'class':'arrange-unit__09f24__rqHTg arrange-unit-fill__09f24__CUubG  border-color--default__09f24__NPAKY'}):
    name=a.find('a', attrs={'class':'css-1m051bw'})
    # city=a.find('span', attrs={'class':'css-chan6m'})
    # ratings=a.find('span', attrs={'class':'css-chan6m'})
    # service=a.find('span', attrs={'class':'display--inline__09f24__c6N_k  border-color--default__09f24__NPAKY'})
    # website=a.find('a', attrs={'class':'platformSearchAction__09f24__PNDZS horizontalSearchAction__09f24__yYw_h css-k6yh4k'})
    companyname.append(name.text)
    # location.append(city.text)
    # reviewcount.append(ratings.text)
    # services.append(service.text)
    # websites.append(website.text)

df=pd.DataFrame({'companyname':companyname})
df.to_csv('yelp.csv', index=False, encoding='utf-8')
    