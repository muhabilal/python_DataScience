import pandas as pd
# print(pd.__version__)
#read the data
df=pd.read_csv('./Data/popultion_of_pakistan.csv')
# print(df)
#write the data
df.to_excel('./Data/awein_data.xlsx')
# reading the excel file
df_excel=pd.read_excel('./Data/awein_data.xlsx')
# print(df_excel)


#how the data looks like
# print(df.info())

# print(df.describe())
