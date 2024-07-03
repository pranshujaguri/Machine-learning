# -*- coding: utf-8 -*-
"""
Created on Wed Jul  3 21:22:56 2024

@author: pranshu jaguri
"""

import pandas as pd

dataset=pd.read_csv('D:\CDAC PG-DBDA Course\Machine learning\Day 4\player.csv')
dataset



a=dataset[dataset['category']=='Bowler']
a

b=dataset[(dataset['Team']=='Mumbai indians')]
b

b=dataset[(dataset['Team']=='Mumbai indians') & (dataset['Runs'] > 3000)]
b

c=dataset[(dataset['Team']=='RCB') | (dataset['Team']=='Chennai Super King')]
c

d=dataset['Bidprice']
d.mean()

e=dataset['Runs']
e.mean()

sorted_dataset=dataset.sort_values(by=['Bidprice','player'],ascending=[True,False])
sorted_dataset

dataset.sort_values('Bidprice',ascending=False).head(1)

f=dataset.groupby('player')['Runs'].sum().tail(1)

g=f['Team']

dataset.sort_values('Runs',ascending=True).head(1)

h=dataset['player'].count()
h

dataset.shape[0]

i=dataset.groupby('Team')['Team'].count()
i.sort_values(ascending=True)


j=dataset.groupby('Team')['Bidprice'].max()
j.sort_values(ascending=True)

k=dataset.groupby('Team')[['player','Bidprice']].max()

k



k1=dataset.groupby('Team')['Runs'].mean()
k1
