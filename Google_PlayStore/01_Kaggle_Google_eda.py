# import pandas as pd
# import ydata_profiling as yd
# df=pd.read_csv('./data/googleplaystore.csv')
# profile=yd.ProfileReport(df)
# profile.to_file(output_file="./outputs/googleplaystore.html")





# import pandas as pd
# import numpy as np
# import seaborn as sns
# import matplotlib.pyplot as plt

# df=pd.read_csv('./data/googleplaystore.csv')


#check the data
# print(df.info())

#lets have a look on the data

# print(df.head())


#to print randomnly 10 data
# print(df.sample(10))
# print(df.describe())

# res=df['Size'].unique()
# print(res)




# Now below is the complete EDA of Google PlayStore DataSet
# 1-import Libararies
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# 2-Data Loading and Exploration | Reading
df=pd.read_csv('./data/googleplaystore.csv')

# 3-lets have a look on top 5 rows
print(df.head())
