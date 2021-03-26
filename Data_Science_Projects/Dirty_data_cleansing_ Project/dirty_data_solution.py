import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('dirty_data.csv')

#naming ID column
df.rename(columns={'Unnamed: 0':'id'},inplace=True)

for i,j in df.iterrows():
        # Correcting 'Uber Type'
        k=int(j['id'][2])
        if k==1:
            df.loc[i,'Uber Type']=0
        elif k==3:
            df.loc[i,'Uber Type']=1
        else:
            df.loc[i,'Uber Type']=2

        # Correcting 'Origin Latitude' and 'Destination Latitude'
        if j['Origin Latitude']>0:
            df.loc[i,'Origin Latitude']=-j['Origin Latitude']
        if j['Destination Latitude']>0:
            df.loc[i,'Destination Latitude']=-j['Destination Latitude']

        # Correcting 'Departure Date' (swaping month & day)
        d=j['Departure Date'].split('-')
        if int(d[1])>12:
            d[1],d[2]=d[2],d[1]
            df.loc[i,'Departure Date']='-'.join(d)

        # Correcting 'Departure Date' (correcting no of days in a month)
        if d[1]=='02' and int(d[2])>28:
            d[2]='28'
            df.loc[i,'Departure Date']='-'.join(d)
        elif int(d[1])%2==0 and int(d[2])>30:
            d[2]='30'
            df.loc[i,' Date']='-'.join(d)

        # Correcting Time - (Swap 'Departure Time' & 'Arrival Time' if Departure > Arrival
        t=list(map(int,j['Departure Time'].split(':')))
        time=t[0]*3600+t[1]*60+t[2]
        t2=list(map(int,j['Arrival Time'].split(':')))
        time2=t2[0]*3600+t2[1]*60+t2[2]
        dif=time2-time
        if dif<0:
            dif+=24*3600
        if dif>6*3600:
           df.loc[i,'Arrival Time']=j['Departure Time']
           df.loc[i,'Departure Time']=j['Arrival Time']
            
df.to_csv('dirty_data_sol.csv',index=0)
