# -*- coding: utf-8 -*-
"""Central_Indian_Rainfall_Assignment.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1RXUK9pqUdpms2ezlXmg9r8OJL_kSqN0i
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import sklearn.metrics as metrics
from sklearn.linear_model import LinearRegression

cir=pd.read_csv('Assignment_Central_India_Rainfall_1901_2016.csv')

cir.head(29)

cir.info()

cir.isnull().sum()

print(cir['Actual Rainfall: JUL'].max())
print(cir['Actual Rainfall: JUL'].min())

print(cir['Actual Rainfall: JUN'].max())
print(cir['Actual Rainfall: JUN'].min())

print(cir['Actual Rainfall: AUG'].max())
print(cir['Actual Rainfall: AUG'].min())

print(cir['Actual Rainfall: SEPT'].max())
print(cir['Actual Rainfall: SEPT'].min())

cir[['YEAR','Actual Rainfall: JUN-SEPT']].groupby('Actual Rainfall: JUN-SEPT').min()

cir.sort_values(by='Actual Rainfall: JUN-SEPT', ascending=True)

"""### Data Visualisation"""

cir[['YEAR','Actual Rainfall: JUN', 'Actual Rainfall: JUL','Actual Rainfall: AUG', 'Actual Rainfall: SEPT']].groupby("YEAR").mean().plot(figsize=(22,15))
plt.xlabel('Year (1901-2016)',fontsize=20)
plt.ylabel('Seasonal Rainfall (in mm)',fontsize=20)
plt.title('Seasonal Rainfall from Year 1901 to 2016',fontsize=25)
plt.grid()

"""In the above figure, I have seen that the rainfall or monsoon season started from the June months with little rainfall in comparison to rest of monsoon 
months. The minimum rainfall occur in month on June in the year of 1923 and maximum was in 1937. In the graph we clearly seen that major proportion of rainfall occur in month on July.
"""

cir[['YEAR','Actual Rainfall: JUN-SEPT']].groupby("YEAR").mean().plot(figsize=(22,15));
plt.xlabel('Year (1901-2016)',fontsize=20)
plt.ylabel('Seasonal Rainfall (in mm)',fontsize=20)
plt.title('Seasonal Rainfall from Year 1901 to 2016',fontsize=25)
plt.grid()

"""If we see the overall rainfall betwenn June and September, the minimum amount of rainfall occur in the year of 1918 with 679.9mm of rainfall, and maximum was in the year of 1994 with 1349.4mm of rainfall. In the graph we can seen that there were lesser amount of rainfall in between 1920 and 1940."""

graph1=cir.groupby("YEAR").mean()['Actual Rainfall: JUN-SEPT'].plot(ylim=(600,1400),color='red',marker='o',linestyle='-',linewidth=3,figsize=(22,8));
plt.xlabel('Year',fontsize=20)
plt.ylabel('Annual Rainfall (in mm)',fontsize=20)
plt.title('Total Rainfall in India between Year 1901 and 2016',fontsize=25)
graph1.tick_params(labelsize=15)
plt.grid()

"""In above graph the rainfall occur in the month of Jun, July, August and September. Sometime high rainfall occur and sometimes low. In graph we didn't find that any year which having no rainfall. The maximum rainfall occur in year of 1994 and minimum is in 1918 and 1987."""

cir.loc[cir.YEAR==2013]

cir[['YEAR', 'Actual Rainfall: JUN', 'Actual Rainfall: JUL',
       'Actual Rainfall: AUG','Actual Rainfall: SEPT']].groupby("YEAR").mean().sort_values('YEAR').plot.bar(width=0.5,edgecolor='k',stacked=True,figsize=(25,8));
plt.xlabel('Year (1901-2016)',fontsize=30)
plt.ylabel('Rainfall (in mm)',fontsize=20)
plt.title('Rainfall from 1901 to 2016 in India',fontsize=25)
plt.grid()

"""This graph clearly depicts the rainfall occur in all four months of every year. In this graph clearly shows that there were no sudden or sharp rise in increase or decrease in rainfall. Which is good sign in terms of global warming. As there is no such effect can be seen of Global Warming."""

graph=cir[['Actual Rainfall: JUN', 'Actual Rainfall: JUL','Actual Rainfall: AUG','Actual Rainfall: SEPT']].mean().plot.bar(width=0.6,linewidth=2,figsize=(22,8))
plt.xlabel('Month',fontsize=30)
plt.ylabel('Monthly Rainfall (in mm)',fontsize=20)
plt.title('Monthly Rainfall in India',fontsize=25)
plt.grid()

"""Above graph is the mean value of the each month from 1901 to 2016.It tells that which month has high amount of rainfall. In graph it shows that rain starting from June month with little rainfall, after that maximum amount of rainfall can be seen in the month of July, which is most. Then slighly decreses in month of August and Septermber, which is end of the monsoon season.

### Splitting the data in Training and Testing
"""

x=cir.drop(['Actual Rainfall: JUN-SEPT'], axis=1).values
y=cir['Actual Rainfall: JUN-SEPT'].values

x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.30, random_state=42)

"""## Linear Regression"""

lr1=LinearRegression()
lr1.fit(x_train,y_train)

y_pred1=lr1.predict(x_test)
y_pred1[0:5]

accuracy = lr1.score(x_test,y_test)
print(accuracy*100,'%')

"""## K Nearest Neighbour Algorithms"""

from sklearn.neighbors import KNeighborsRegressor
from sklearn.preprocessing import StandardScaler    
st_x= StandardScaler()

x_train= st_x.fit_transform(x_train)    
x_test= st_x.transform(x_test)

knn = KNeighborsRegressor(n_neighbors=1)
knn.fit(x_train, y_train)

y_pred= knn.predict(x_test)

y_pred[0:5]

y_test[0:5]

knn.score(x_test, y_test)

k_range = range(1, 31)
values = []
for k in k_range:
    knn = KNeighborsRegressor(n_neighbors=k)
    knn.fit(x_train, y_train)
    y_pred = knn.predict(x_test)
    values.append(knn.score(x_test, y_test))
print(values)

plt.plot(k_range, values)
plt.xlabel('Value of K for KNN')
plt.ylabel('Testing Accuracy')

"""When I increase the 'n_neighbor' value from 1 to onwards, the accuracy started decreasing."""