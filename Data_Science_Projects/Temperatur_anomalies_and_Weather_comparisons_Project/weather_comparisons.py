import pandas as pd
pd.set_option('chained_assignment',None)

data=pd.read_csv('lokka.txt',sep='\s+',na_values='-9999',engine='python')
data['TMAX']=data['TMAX'].astype(float)
data['TMIN']=data['TMIN'].astype(float)

# Adding column 'TAVG'
data['TAVG']=(data.TMAX +data.TMIN)/2

# Calculating the monthly temperature anomalies in Sodankyla and adding column 'TempsC'
sel=data[['DATE','TAVG']]
sel['DATE']=sel['DATE'].astype(int)
sel['DATE']//=100
monthlyData=sel.groupby('DATE').mean()
monthlyData['TempsC']=(monthlyData['TAVG']-32)*5/9

ref=pd.DataFrame()
ref['DATE']= monthlyData.index
ref['TempsC']= monthlyData['TempsC'].values
ref['DATE']%=100
referenceTemps=ref.groupby('DATE').mean()

# Calculate the monthly temperature differences
df=pd.read_csv('Helsinki.csv')
print(df)
diff=referenceTemps.copy()
diff['TempsC']=df['TempsC']+diff['TempsC']

# difference in the summer temperatures btw stations
d=diff.loc[[5,6,7]]

# saving it
diff.to_csv('Monthly diff.csv')

# Summer mean & std temperatures for both stations
print('mean & std for summer in Helsinki : ',df.loc[[5,6,7],'TempsC'].mean(),df.loc[[5,6,7],'TempsC'].std())
print('mean & std for summer in Sodankyla: ',referenceTemps.loc[[5,6,7],'TempsC'].mean(),referenceTemps.loc[[5,6,7],'TempsC'].std())

