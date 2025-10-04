import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --- Step 1: Load dataset ---
df = pd.read_csv("carData.csv")
# print(df.head())
# print(df.info())

# --- Step 2: Basic EDA ---
# print(df.describe())

# Check missing values
# print(df.isnull().sum())

# Drop rows with missing values
# df = df.dropna()

#extract brand from name
df['brand'] = df['name'].apply(lambda x: x.split()[0])  # Get first word as brand
df = df.drop('name', axis=1)

#---- extract numeric value, remove text units
def extract_numeric(value):
    """Extracts numeric part from strings like '74 bhp' or '1248 CC'."""
    try:
        return float(str(value).split()[0])
    except:
        return np.nan

# print(df['max_power'].tail())
# print(df['max_power'].dtype)

#data types changed from objects to numeric
cols_to_clean = ['mileage(km/ltr/kg)', 'engine', 'max_power']

for col in cols_to_clean:
    df[col] = df[col].apply(extract_numeric)

# print(df['max_power'].dtype)


#Fill missing values
df = df.fillna({
    'mileage(km/ltr/kg)': df['mileage(km/ltr/kg)'].median(),
    'engine': df['engine'].median(),
    'max_power': df['max_power'].median(),
    'seats': df['seats'].median()
})

print(df.dtypes)
print(df.isnull().sum())
