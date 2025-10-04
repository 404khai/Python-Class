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


plt.figure(figsize=(8,5))
sns.histplot(df['selling_price'], bins=30, kde=True)
plt.title("Distribution of Selling Price")
plt.show()

plt.figure(figsize=(8,5))
sns.scatterplot(x='km_driven', y='selling_price', data=df)
plt.title("Selling Price vs KM Driven")
plt.show()

# --- Step 5: Prepare features ---
X = df.drop('selling_price', axis=1)
y = df['selling_price']

# Identify numeric and categorical columns
numeric_features = ['km_driven', 'mileage(km/ltr/kg)', 'engine', 'max_power', 'seats']
categorical_features = ['fuel', 'seller_type', 'transmission', 'owner', 'brand']


# --- Step 6: Preprocessing ---
numeric_transformer = Pipeline(steps=[
    ('scaler', StandardScaler())
])

categorical_transformer = Pipeline(steps=[
    ('encoder', OneHotEncoder(handle_unknown='ignore'))
])

preprocessor = ColumnTransformer(
    transformers=[
        ('num', numeric_transformer, numeric_features),
        ('cat', categorical_transformer, categorical_features)
    ]
)

# --- Step 7: Split data ---
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# --- Step 8: Train models ---
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42)
}

results = {}

for name, model in models.items():
    pipe = Pipeline(steps=[('preprocessor', preprocessor),
                           ('model', model)])
    
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)
    
    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    
    results[name] = {"MSE": mse, "MAE": mae, "R2": r2}
    
    print(f"\n📊 {name} Results:")
    print(f"MAE: {mae:.2f}")
    print(f"MSE: {mse:.2f}")
    print(f"R²: {r2:.2f}")
    
    # Plot Actual vs Predicted
    plt.figure(figsize=(6,4))
    sns.scatterplot(x=y_test, y=y_pred, alpha=0.6)
    plt.xlabel("Actual Selling Price")
    plt.ylabel("Predicted Selling Price")
    plt.title(f"Actual vs Predicted - {name}")
    plt.show()

# --- Step 9: Compare results ---
results_df = pd.DataFrame(results).T
print("\nModel Comparison:")
print(results_df)

sns.barplot(x=results_df.index, y=results_df['R2'])
plt.title("Model R² Comparison")
plt.show()