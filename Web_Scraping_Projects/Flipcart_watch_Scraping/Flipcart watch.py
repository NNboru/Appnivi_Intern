import pandas as pd

from urllib.request import urlopen

from bs4 import BeautifulSoup as bs

url='https://www.flipkart.com/mens-watches-store?otracker=nmenu_sub_Men_0_Watches'

# opening url
html=urlopen(url)

# reading content from html
soup=bs(html,'lxml')

# retrieving required data
a=soup.find_all('a',class_='_2cLu-l')
b=soup.find_all('div',class_='_1vC4OE')
b=soup.find_all('div',class_='_1vC4OE')
c=soup.find_all('span',class_='_1vC4OE')

# making dataFrame
df=pd.DataFrame({'Name':[i.text for i in a],'Price':[i.text for i in b]})

#df.to_csv('watch.csv',index=0)
print(df)

