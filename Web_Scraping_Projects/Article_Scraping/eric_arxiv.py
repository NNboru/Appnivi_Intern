import pandas as pd

from urllib.request import urlopen

from bs4 import BeautifulSoup as bs

inp=input('Enter Name: ')
name='+'.join(inp.split())
url=f'https://arxiv.org/search/?query={name}&searchtype=all&abstracts=show&order=-announced_date_first&size=25'
u=f'https://eric.ed.gov/?q={name}'

df=pd.DataFrame(columns=['Heading','Author','Co-Authors','Link'])

# taking data from arxiv.org
html=urlopen(u)
soup=bs(html,'lxml')

a=soup.find_all('li',class_='arxiv-result')
for b in a:
    if(len(df)==10):break
    link=b.find('p',class_='list-title is-inline-block').find('a')['href']
    text=b.find('p',class_='title is-5 mathjax').text.strip()
    ath=b.find('p',class_='authors').find_all('a')
    sub='; '.join([i.text for i in ath[1:]])
    df.loc[len(df)]=[text,ath[0].text,sub,link]

# taking data from eric.ed.gov
html=urlopen(u)
soup=bs(html,'lxml')

a=soup.find_all('div',class_='r_i')
for b in a:
    if(len(df)==20):break
    link=b.find('div',class_='r_t').find('a')['href']
    text=b.find('div',class_='r_t').find('a').text.strip()
    ath=b.find('div',class_='r_a').text.split('–')[0].split(';')
    sub='; '.join(ath[1:])
    df.loc[len(df)]=[text,ath[0],sub,link]


# display data
col=df.columns
for i,row in df.iterrows():
    print(f'HEADING {i+1}:\n {row[col[0]]}')
    print(col[1].upper(),': ',row[col[1]])
    print(col[2].upper(),': ',row[col[2]])
    print(col[3].upper(),': ',row[col[3]],f'\n{"-"*30}\n')





