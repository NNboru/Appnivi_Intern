import pandas as pd

from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup as bs

page='https://catalog.data.gov/dataset'

# Problem 1
try:
    html=urlopen(page)
except:
    print('Page Not Found')
else:
    print('Page Found')

# Problem 2
soup=bs(urlopen('https://en.wikipedia.org/robots.txt'),'lxml')
print(soup.text)

# Problem 3
soup=bs(html,'lxml')
a=soup.find('div',class_='new-results')
print(a.text.strip())

# Problem 4 , Not working because it requires API key.
page1='http://maps.googleapis.com/maps/api/geocode/json'
rq=requests.get(page1,{'address': "1600 Amphitheatre Parkway, Mountain View, CA"})

# Problem 5
page2='https://catalog.data.gov/dataset?q=&sort=metadata_created+desc&as_sfid=AAAAAAW1VWQPsO0yeyOJ-VYVubDMK1EMmfGUYpH0yjyatG6VhWyUna1-j9dM9iX0q_XEUK3YPfei2m6Rq0ngDLdNdUYVeDbLGSKKrVJUWIzgystjryCA3zwUjdMedmp4jqBHmko%3D&as_fid=0f3d4023baa02bf87ffe4bd6202616e52ef7a675&ext_location=&ext_bbox=&ext_prev_extent=-142.03125%2C8.754794702435618%2C-59.0625%2C61.77312286453146'
soup=bs(urlopen(page2),'lxml')
a=soup.find('h3',class_='dataset-heading')
print(a.text)

# Problem 6
page3='https://example.com/'
soup=bs(urlopen(page3),'lxml')
a=soup.find('h1')
print(a.text)

# Problem 7
page4='https://en.wikipedia.org/wiki/Main_Page'
soup=bs(urlopen(page4),'lxml')
a=soup.find_all(['h1','h2','h3','h4','h6'])
for i in a:
    print (i.name,':',i.text)

# Problem 8
page5='https://en.wikipedia.org/wiki/Peter_Jeffrey_(RAAF_officer)'
soup=bs(urlopen(page5),'lxml')
a=soup.find_all('img')
for i in a:
    print(i['src'])

# Problem 9
rq=requests.get('https://www.data.gov/')
r = requests.get("https://analytics.usa.gov/data/live/browsers.json")
print("90 days of visits broken down by browser for all sites:")
print(r.json()['totals']['browser'])

# Problem 10
page6='https://en.wikipedia.org/wiki/Python'
soup=bs(urlopen(page6),'lxml')
from random import choice
while 1:
    try:
        a=choice(soup.find_all('a'))
        soup=bs(urlopen(a['href']),'lxml').find_all('a')
        break
    except:
        pass
print("Random url is: ",a['href'])
for s in soup:
    print(s.prettify())




