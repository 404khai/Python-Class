import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("titanic.csv")

# print("Shape of dataset: ", df.shape)

# print("\n First five rows \n",df.head())
# print("\n Dataset Info. \n")
# print(df.info())
# print("\n Summary Statistics (numeric columns)\n", df.describe())

#get missing values
print("\n Missing values\n", df.isnull.sum())



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

