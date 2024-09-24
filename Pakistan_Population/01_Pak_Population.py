import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#import datset
df=pd.read_csv("./data.csv")
# print(df.head())



#1-Explore the data(Composition)
# print(df.info())

pd.set_option('display.max_columns',None)
# print(df.head())


#see all columns names once
# print(df.columns)

#lets have a look on dataTypes
# print(df.dtypes)


#Summary Statistics
# print(df.describe())



#how many are the missing values
print(df.isnull().sum())


#2- Box Plot
sns.boxplot(df,x='AREA (sq.km)')
# plt.show()


sns.boxplot(df,x='DIVISION',y='ALL SEXES (RURAL)')
# plt.show()


# it is very hard to plot therefore we will use groupby function to make tabulated data output
# print(df['DISTRICT'].nunique())
# print(df.groupby(['DIVISION']).size().sort_values())
# print(df.groupby('DIVISION')['ALL SEXES (RURAL)'].mean())
res=df.groupby(['PROVINCE','DIVISION','DISTRICT','SUB DIVISION'])['ALL SEXES (RURAL)'].mean()
print(res)


