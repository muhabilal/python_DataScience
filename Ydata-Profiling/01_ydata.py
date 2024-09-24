#Automatic EDA using ydata-profiling
import pandas as pd
import seaborn as sns
import ydata_profiling as yd


#import data from seaborn
df=sns.load_dataset('titanic')
profile=yd.ProfileReport(df)
# profile.to_file(output_file="./outputs/ydata_titanic.html")




#do it on our Pak Population Dataset
df_pop=pd.read_csv("data.csv")
profile=yd.ProfileReport(df_pop)
profile.to_file(output_file="./outputs/ydata_population.html")