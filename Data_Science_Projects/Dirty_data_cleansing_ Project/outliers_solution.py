import pandas as pd
import matplotlib.pyplot as plt

def plot(x):
    plt.scatter(df.index,df[x])
    plt.show()
df=pd.read_csv('outliers.csv')

def Remove(row, var=1):
    global df
    d = df[row].mean() , var*df[row].std()
    df=df[ (df[row]> d[0]-d[1]) & (df[row]< d[0]+d[1]) ]


# Removing outliers from - 'Fare$'
Remove('Fare$')

# Removing outliers from - 'Origin Latitude'
Remove('Origin Latitude')

# Removing outliers from - 'Destination Latitude'
Remove('Destination Latitude')

df.to_csv('outliers_solution.csv',index=False)

