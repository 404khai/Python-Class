import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# Step 1: Load dataset
df = pd.read_csv("housing.csv")  # UCI/Kaggle California Housing dataset
print(df.head())
print(df.info())

# Step 2: Basic EDA
print(df.describe())

sns.histplot(df["median_house_value"], bins=50, kde=True)
plt.title("Distribution of House Prices")
plt.show()

# Step 3: Features & Target
X = df.drop("median_house_value", axis=1)
y = df["median_house_value"]

# Step 4: Handle missing values
X["total_bedrooms"] = X["total_bedrooms"].fillna(X["total_bedrooms"].median())

# Step 5: Identify numeric & categorical columns
numeric_features = [
    "median_income",
    "housing_median_age",
    "total_rooms",
    "total_bedrooms",
    "population",
    "households",
    "latitude",
    "longitude",
]
categorical_features = ["ocean_proximity"]

# Preprocessing
numeric_transformer = Pipeline(steps=[("scaler", StandardScaler())])

categorical_transformer = Pipeline(
    steps=[("encoder", OneHotEncoder(handle_unknown="ignore"))]
)

preprocessor = ColumnTransformer(
    transformers=[
        ("num", numeric_transformer, numeric_features),
        ("cat", categorical_transformer, categorical_features),
    ]
)

# Step 6: Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Step 7: Models
models = {
    "Linear Regression": LinearRegression(),
    "Random Forest": RandomForestRegressor(n_estimators=100, random_state=42),
}

results = {}

# Step 8: Train & Evaluate
for name, model in models.items():
    pipe = Pipeline(steps=[("preprocessor", preprocessor), ("model", model)])
    pipe.fit(X_train, y_train)
    y_pred = pipe.predict(X_test)

    mse = mean_squared_error(y_test, y_pred)
    mae = mean_absolute_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)

    results[name] = {"MSE": mse, "MAE": mae, "R2": r2}
    print(f"\n🔹 {name} Results:")
    print("MSE:", mse)
    print("MAE:", mae)
    print("R² Score:", r2)

    # Plot Actual vs Predicted
    plt.scatter(y_test, y_pred, alpha=0.5, label=name)
    plt.xlabel("Actual Prices")
    plt.ylabel("Predicted Prices")
    plt.title(f"Actual vs Predicted - {name}")
    plt.legend()
    plt.show()

# Step 9: Compare Results
results_df = pd.DataFrame(results).T
print("\n📊 Model Comparison:")
print(results_df)

sns.barplot(x=results_df.index, y=results_df["R2"])
plt.title("R² Comparison of Models")
plt.ylabel("R² Score")
plt.show()