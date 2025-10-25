
# Sales prediction (Advertising) — Linear Regression example
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score

# 1) Load dataset
dataset = pd.read_csv('Advertising.csv')       
dataset = dataset.drop(columns=['Unnamed: 0'], errors='ignore')  # drop index column if exists

# Quick look
print("Shape:", dataset.shape)
print(dataset.head())

# 2) Prepare features (X) and target (y)
X = dataset.iloc[:, :-1]   # all columns except last (TV, Radio, Newspaper)
y = dataset.iloc[:, -1]    # last column (Sales)

# 3) Exploratory plots
print("\nCorrelation matrix:\n", dataset.corr())
sns.pairplot(dataset)      # visual relationships between features and target
plt.show()

# 4) Train / test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.20, random_state=43
)
print("\nX_train shape:", X_train.shape, "X_test shape:", X_test.shape)

# 5) Scaling (fit scaler on train only, then transform train and test)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)   # learn scaling from training data
X_test_scaled = scaler.transform(X_test)         # apply same scaling to test data

# 6) Build and fit Linear Regression model
lr = LinearRegression()
lr.fit(X_train_scaled, y_train)                  # training the model

# 7) Predictions
y_pred = lr.predict(X_test_scaled)
y_pred

# 8) Model coefficients (interpretable in scaled-space)
coefficients = pd.Series(lr.coef_, index=X.columns)
print("\nIntercept:", lr.intercept_)
print("Coefficients:\n", coefficients)

# 9) Evaluation metrics
mse = mean_squared_error(y_test, y_pred)
mae = mean_absolute_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

# {metrice:.4f} is decreasing the overflow decimal number
print(f"\nMSE: {mse:.4f}")
print(f"MAE: {mae:.4f}")
print(f"R2 score: {r2:.4f}")

# 10) Plots: True vs Predicted and Residuals
plt.figure(figsize=(6,4))
plt.scatter(y_test, y_pred, label='Predicted (test)', marker='x')
plt.plot([y.min(), y.max()], [y.min(), y.max()], 'k--', label='Perfect prediction')
plt.xlabel("True Sales")
plt.ylabel("Predicted Sales")
plt.title("True vs Predicted Sales")
plt.legend()
plt.show()

residuals = y_test - y_pred
plt.figure(figsize=(6,4))
plt.scatter(y_pred, residuals)
plt.axhline(0, color='k', linestyle='--')
plt.xlabel("Predicted Sales")
plt.ylabel("Residuals (True - Predicted)")
plt.title("Residuals vs Predicted")
plt.show()
