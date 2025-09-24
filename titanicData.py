import pandas as pd

df = pd.read_csv("titanic.csv");

# See last 5 rows
# print(df.head(3))

# See last 5 rows
# print(df.tail())

# print(df.isnull().sum())

# df["Age"].fillna(df["Age"].median(), inplace=True)
# print(df.describe)