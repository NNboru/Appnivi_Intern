import pandas as pd

data=pd.read_csv(r'6153237444115dat.csv',na_values=['*', '**', '***', '****', '*****', '******'])

#problem 1
print(len(data))

print(data.columns)

print(data.dtypes)
    
print(data['TEMP'].mean())

print(data['MAX'].std())

print(len(data['USAF'].unique()))

#problem 2

selected=data[['USAF', 'YR--MODAHRMN', 'TEMP', 'MAX', 'MIN']]

selected=selected.dropna(subset=['TEMP'])

selected['celsius']=[(i-32)*9/5 for i in selected['TEMP']]

selected['celsius']=round(selected['celsius'])

selected['celsius']=selected['celsius'].astype(int)

#problem 3

kumpula=selected[selected['USAF']==29980]

rovaniemi=selected[selected['USAF']==28450]

kumpula.to_csv('Kumpula_temps_May_Aug_2017.csv',float_format='%.2f')

rovaniemi.to_csv('rovaniemi_temps_May_Aug_2017.csv',float_format='%.2f')

#problem 4

    #**Part 1**
print('median kumpala   of temp: ',kumpula['TEMP'].median())
print('median rovaniemi of temp: ',rovaniemi['TEMP'].median())

    #**Part 2**
kumpula_may=kumpula[kumpula['YR--MODAHRMN']//1000000==201705]
rovaniemi_may=rovaniemi[rovaniemi['YR--MODAHRMN']//1000000==201705]

kumpula_june=kumpula[kumpula['YR--MODAHRMN']//1000000==201706]
rovaniemi_june=rovaniemi[rovaniemi['YR--MODAHRMN']//1000000==201706]

print('mean min max of kumpala   temp in may: ',kumpula_may['TEMP'].mean(),kumpula_may['TEMP'].min(),kumpula_may['TEMP'].max())
print('mean min max of rovaniemi temp in may: ',rovaniemi_may['TEMP'].mean(),rovaniemi_may['TEMP'].min(),rovaniemi_may['TEMP'].max())

print('mean min max of kumpala   temp in june: ',kumpula_june['TEMP'].mean(),kumpula_june['TEMP'].min(),kumpula_june['TEMP'].max())
print('mean min max of rovaniemi temp in june: ',rovaniemi_june['TEMP'].mean(),rovaniemi_june['TEMP'].min(),rovaniemi_june['TEMP'].max())

print('There is about 7% diff in kumpala whereas 14% diff in rovaniemi btw May and June.')
print('Rovaniemi is much colder in may but not in june.')

#problem 5
sel=rovaniemi[['YR--MODAHRMN','TEMP']]
sel['YR--MODAHRMN']//=100
kum=sel.groupby('YR--MODAHRMN')
l1= [ (x,y['TEMP'].mean(),y['TEMP'].max(),y['TEMP'].min()) for x,y in kum]
df=pd.DataFrame(l1,columns=('hour','mean','max','min'))

print(df)


