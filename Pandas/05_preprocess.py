import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# data import
df=sns.load_dataset("titanic")


#check the data
# print(df.head())

#missing values and imputing them
#find out the percentage of missing values
missing_values=df.isnull().sum()/len(df)*100
# print(missing_values)

#1- drop the deck column from the dataset(drop the column having more than 70% of missing vales in dataset)
#axis=1 means that whole column if axis=0 just for row
#inplace=true means that change in the dataset or update the dataset 
drop_column=df.drop("deck",axis=1,inplace=True)
# print(drop_column)
# print(df.columns)

#2- filling the missing values of age column by mean of age
# in mode [3,8] most repated values 0 for 3 and 1 for 8
mean_age1=df['age'].mean()
mean_age2=df['age'].median()
mean_age3=df['age'].mode()[0]
# print(mean_age1)
df["age"].fillna(mean_age1,inplace=True)
# print(df.isnull().sum())


#3- fill embarked and embark_town with mode
df['embarked'].fillna(df['embarked'].mode()[0], inplace=True)
df['embark_town'].fillna(df['embark_town'].mode()[0],inplace=True)
# print(df.isnull().sum())
sns.heatmap(df.isnull())
# plt.show()



#Binning
# print(df.head())
# print(df.age.min())
# print(df.age.max())
sns.histplot(df['age'])
# plt.show()
bins=[0,1,5,12,18,30,50,80]
labels=["Infants","Toddlers","Kids","Teens","Youngs","Middle Age","Old"]
#kis column ko bins mein convert krna hai
pd.cut(df['age'],bins=bins, labels=labels)

#Feature Engineering
df['bined_age']=pd.cut(df['age'],bins=bins, labels=labels)
# print(df.head())
# print(df['bined_age'].value_counts())


#rename a column
df.rename(columns={'bined_age':'age_group'},inplace=True)
# print(df.head())


#data filteration
# print(df.columns)
df_01=df[['survived','age_group','fare','class']]
# print(df_01.head())
# print(df_01.info())
print(df['class'].value_counts())

#filter the data based on rows criteria
df_first=df_01[df_01['class']=='First']
# print(df_first)
# print(df['fare'].min())
# print(df['fare'].max())



#lets select only those rows which have paid more than 200 pounds
df_200=df_01[df_01['fare']>200]
# print(df_200.info())
df_200['class'].value_counts()