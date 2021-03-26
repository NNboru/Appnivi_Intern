import pandas as pd
pd.set_option('chained_assignment',None)

data=pd.read_csv('1091402.txt',sep='\s+',na_values='-9999')
data=data.drop(0)
data['TMAX']=data['TMAX'].astype(float)
data['TMIN']=data['TMIN'].astype(float)
data['TAVG']=data['TAVG'].astype(float)

# Problem 1
print(data['TAVG'].count())

print(data['TMIN'].count())

print(data['DATE'].unique().size)

print(data[0:1])

print(data[-1:])

print(data['TAVG'].mean())

s=0
j=0
t=data['TMAX'].values
for i in data['DATE']:
    if i[2:4]=='69' and int(i[5])>4 and int(i[5])<9:
        s=max(s,t[j])
    j+=1
print(s)

# Problem 2
sel=data[['DATE','TAVG']]
sel['DATE']=sel['DATE'].astype(int)
sel['DATE']//=100
monthlyData=sel.groupby('DATE').mean()
monthlyData['TempsC']=(monthlyData['TAVG']-32)*5/9


# Problem 3
ref=pd.DataFrame()
ref['DATE']= monthlyData.index
ref['TempsC']= monthlyData['TempsC'].values
ref['DATE']%=100
referenceTemps=ref.groupby('DATE').mean()

sel= monthlyData['TempsC'].values.copy()
se = monthlyData.index
for i in range(len(sel)):
    sel[i]-=referenceTemps.loc[se[i]%100]
monthlyData['diff']=sel

referenceTemps.to_csv('Helsinki.csv')
    








             
