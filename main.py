import pandas as pd

df = pd.read_csv("Telco-Customer-Churn.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())

df.isnull().sum()