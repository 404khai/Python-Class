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
# print("\n Missing values\n", df.isnull().sum())


#handle missing values
# df["Age"].fillna(df["Age"].median(), inplace=True)
# print("\n Missing values\n", df.isnull().sum())

# df["Embarked"].fillna(df["Embarked"].mode()[0], inplace=True)
# df.drop(columns="Cabin", inplace=True)

# print("\n Value count for survived", df["Survived"].value_counts())
# print("\n Gender count for people", df["Sex"].value_counts())


# Visualize the distribution of survivors
sns.countplot(x="Survived", data=df)
plt.title("Survival Count (0 = Died | 1 = Survived)")
plt.show()

sns.countplot(x='Sex', hue='Survived', data=df)
plt.title("Survival by Gender")
plt.show()

sns.histplot(df['Age'], bins=30, kde=True)
plt.title("Age Distribution")
plt.show()

sns.boxplot(x='Pclass', y='Age', data=df)
plt.title("Age Distribution by Passenger Class")
plt.show()

plt.figure(figsize=(8, 6))
sns.heatmap(df.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

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

