import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('missing_value.csv')

df.rename(columns={'Unnamed: 0':'id'},inplace=True)

# filling - 'Uber Type'
for i,j in df.iterrows():
    if pd.isna(j['Uber Type']):
        k=int(j['id'][2])
        if k==1:
            df.loc[i,'Uber Type']=0
        elif k==3:
            df.loc[i,'Uber Type']=1
        else:
            df.loc[i,'Uber Type']=2


# filling - 'Fare$'
df['Fare per m']=df['Fare$']/df['Journey Distance(m)']
dg= df.groupby('Uber Type').mean()['Fare per m']

for i,j in df.iterrows():
    if pd.isna(j['Fare$']):
        df.loc[i,'Fare$']=dg[j['Uber Type']]*j['Journey Distance(m)']

df.drop('Fare per m',axis=1,inplace=True)
df.to_csv('missing_value_solution.csv',index=False)
