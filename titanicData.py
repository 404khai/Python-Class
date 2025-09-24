import pandas as pd

df = pd.read_csv("titanic.csv");

# See last 5 rows
# print(df.head(3))

# See last 5 rows
# print(df.tail())

# print(df.isnull().sum())

# df["Age"].fillna(df["Age"].median(), inplace=True)
# print(df.describe)


# df.drop("Cabin", axis=1, inplace=True)
# df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)

# #drop irrelevant columns
# df.drop(["PassengerId", "Name", "Ticket"], axis=1, inplace=True)
# #mapping strings in a column of data to number values
# df["Sex"] = df["Sex"].map({"male": 0, "female": 1})

