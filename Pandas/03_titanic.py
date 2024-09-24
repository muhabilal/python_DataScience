import pandas as pd
import numpy as np
import seaborn as sns

df=sns.load_dataset('titanic')
# print(df)

#summary
# print(df.describe())

#reverse row order
# print(df.loc[::-1].head())

#reverse column order
# print(df.loc[:,::-1].head())

#select a column by data type
# print(df.dtypes)


# only select those who having numeric type
# print(df.select_dtypes(include=["number"]).head())


# only select those who having object type
# print(df.select_dtypes(include=["object"]).head())



# only select those who having object and number type
# print(df.select_dtypes(include=["object","number"]).head())

# only select those who having object and number type
# print(df.select_dtypes(exclude=["object","number"]).head())

#convert string to numebers
df=pd.DataFrame({
    "col_a":[1,2,3,4,5,6],
    "col_b":[7,8,9,10,11,12]
})
# print(df.dtypes)
convert=df.astype({'col_a':'float64','col_b':'float64'}).dtypes
print(convert)

print(pd.to_numeric(df['col_a'],errors="coerce").dtype)