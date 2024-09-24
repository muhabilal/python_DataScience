import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

#load the dataset
df=sns.load_dataset('titanic')
# print(df.head())

#basic information
# print(df.info())

#finding missing values/ null values/ nan values
# print(df.isnull().sum())

#percentage of missing values in a column
# print(df.isnull().sum()/len(df)*100)

#Another way to see the missing values
res=sns.heatmap(df.isnull())
# plt.show()


#unique values
# print(df['sex'].unique())
#nunique means number of unique values
# print(df['sex'].nunique()) 
#to find all the unique values
# print(df.nunique())


#to slect one column by name
# print(df["sex"])

#to slect two columns by name
# print(df[["sex","age"]])



#to print the columns names
# print(df.columns)

#to count values of the column
# print(df['embark_town'].value_counts())



# to find mean fare of both  male and female bu using groupby
# print(df.groupby('sex')['fare'].mean())
# print(df.groupby('class')['fare'].mean())
# print(df.groupby(['survived','sex'])['fare'].mean())
# print(df.groupby(['survived','who'])['fare'].mean())
# print(df.groupby(['survived','who']).size())




#correlation matrix
correlation_df=df[['fare','age','sibsp','parch']].corr()
sns.heatmap(correlation_df, annot=True)
# plt.show()

sns.pairplot(df)
plt.show()




