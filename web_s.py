from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
#import requests

#f=requests.get("https://www.zillow.com/on/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A62.85036247358242%2C%22east%22%3A-57.66787849999999%2C%22south%22%3A32.12953182007062%2C%22west%22%3A-111.80850349999999%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A404375%2C%22regionType%22%3A2%7D%5D%2C%22usersSearchTerm%22%3A%22Ontario%22%2C%22schoolId%22%3Anull%7D")

driver = webdriver.Chrome("/usr/bin/chromedriver_linux64/chromedriver")

houses=[]
prices=[]
location=[]
driver.get("https://www.zillow.com/on/?searchQueryState=%7B%22mapBounds%22%3A%7B%22north%22%3A62.85036247358242%2C%22east%22%3A-57.66787849999999%2C%22south%22%3A32.12953182007062%2C%22west%22%3A-111.80850349999999%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22sort%22%3A%7B%22value%22%3A%22globalrelevanceex%22%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A4%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A404375%2C%22regionType%22%3A2%7D%5D%2C%22usersSearchTerm%22%3A%22Ontario%22%2C%22schoolId%22%3Anull%7D")

content=driver.page_source
soup=BeautifulSoup(content, 'html.parser')
for i in soup.findAll('div', attrs={'class':'StyledPropertyCardDataWrapper-c11n-8-85-1__sc-1omp4c3-0 jVBMsP property-card-data'}):
    #house=i.find('span', attrs={'class':'StyledPropertyCardTitle-sc-1fcmfeb-0 kLlJyR property-card-title'})
    price=i.find('span', attrs={'data-test':'property-card-price'})
    loc=i.find('address', attrs={'data-test':'property-card-addr'})
    #houses.append(house.text)
    prices.append(price.text)
    location.append(loc.text)

    
df=pd.DataFrame({'price':prices, 'location':location})
df.to_csv('houses.csv', index=False, encoding='utf=8')