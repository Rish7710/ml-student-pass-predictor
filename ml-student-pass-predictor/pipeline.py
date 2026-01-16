import csv
import pandas as pd
df=pd.DataFrame({"age":[23,46,None,76],
    "salary":[45000,50000,None,30000],
    "experience":[2,3,None,1] 
})
df.info()
df.isna().sum()



class DataPipeline:
 def __init__(self,df):
   self.df=df
 def clean(self):
     
     self.df["age"]=self.df["age"].fillna(self.df["age"].mean())
     self.df["salary"]=self.df["salary"].fillna(self.df["salary"].mean())
     self.df["experience"]=self.df["experience"].fillna(0)
     return df
 def engineer(self):
     self.df["salary_per_age"]=self.df["salary"]/self.df["age"]
     self.df=self.df[self.df["experience"]>0]
     return df   
pipeline=DataPipeline(df) 
df=pipeline.clean()
df=pipeline.engineer()
df.to_csv("cleaned_users.csv",index=False)     
print(df)
     