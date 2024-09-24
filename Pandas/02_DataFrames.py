import pandas as pd
import numpy as np
df=pd.DataFrame(
{"a" : [4, 5, 6],
"b" : [7, 8, 9],
"c" : [10, 11, 12]})
# print(df)



#random
data=pd.DataFrame(np.random.rand(10,2))
# print(data)
data=pd.DataFrame(np.random.rand(4,8),columns =list("ABCDEFGH"))
# print(data)

#how to rename columns
df=pd.DataFrame(
{"col a" : [4, 5, 6],
"col b" : [7, 8, 9],
"col c" : [10, 11, 12]})
change_spell=df.rename(columns={'col a':'col_a','col b':'col_b','col c':'col_c'})
# print(change_spell)
df.columns=['a','b','c']
print(df)

