# Employees data cleaning
import numpy as np
import pandas as pd
df=pd.read_csv("employees_1.csv")
print(df)
print(df.info())
print(df.describe())
print(df.isnull().sum())

df = df.dropna(subset=["EmployeeID"])
print(df)

df["Name"]=df["Name"].str.strip().str.title()
df["Name"]=df["Name"].fillna("Unknown")
print(df)

df["Email"]=df["Email"].str.strip().str.lower()
df["Email"]=df["Email"].fillna("no_email")
print(df)

invalid_salary=(df["Salary"]<= 0) | (df["Salary"] > 200000)
print(invalid_salary)
df.loc[invalid_salary,"Salary"]=np.nan
df["Salary"]=df["Salary"].fillna(df["Salary"].mean())
print(df["Salary"])
print(df)

df["JoinDate"]=pd.to_datetime(df["JoinDate"],format="mixed",dayfirst=True)
print(df["JoinDate"])
df["JoinDate"]=df["JoinDate"].fillna(df["JoinDate"].mode()[0])
print(df["JoinDate"])
print(df)

df["Phone"]=df["Phone"].str.replace("-","")
df["Phone"]=df["Phone"].str.replace(" ","")
df["Phone"]=df["Phone"].fillna("unknown")
print(df["Phone"])
print(df)
print(df.isnull().sum())