import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

from preprocessing import preprocess_data


# Load data
df = preprocess_data("data/raw/inventory_data.csv")

# Features and Target
X = df.drop("Units_Sold", axis=1)
y = df["Units_Sold"]

# Train Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# ----------------------------
# Linear Regression
# ----------------------------

lr = LinearRegression()
lr.fit(X_train, y_train)

lr_predictions = lr.predict(X_test)

print("\nLinear Regression")
print("MAE :", mean_absolute_error(y_test, lr_predictions))
print("RMSE:", mean_squared_error(y_test, lr_predictions) ** 0.5)
print("R2  :", r2_score(y_test, lr_predictions))

# ----------------------------
# Random Forest
# ----------------------------

rf = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

rf.fit(X_train, y_train)

rf_predictions = rf.predict(X_test)

print("\nRandom Forest")

print("MAE :", mean_absolute_error(y_test, rf_predictions))
print("RMSE:", mean_squared_error(y_test, rf_predictions) ** 0.5)
print("R2  :", r2_score(y_test, rf_predictions))

# ----------------------------
# Save Best Model
# ----------------------------

joblib.dump(rf, "models/demand_model.pkl")

print("\nModel saved successfully!")