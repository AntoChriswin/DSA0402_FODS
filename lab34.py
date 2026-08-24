import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Car dataset
data = {
    "Engine_Size": [1.2, 1.5, 1.8, 2.0, 2.2, 2.5, 3.0, 3.5],
    "Horsepower": [80, 100, 120, 140, 160, 180, 220, 250],
    "Mileage": [20, 18, 17, 16, 15, 14, 12, 10],
    "Price": [10000, 13000, 16000, 19000,
              22000, 26000, 32000, 38000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Engine_Size", "Horsepower", "Mileage"]]
y = df["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.25, random_state=42
)

# Train model
model = LinearRegression()
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", round(mse, 2))
print("R2 Score:", round(r2, 2))

# Feature coefficients
print("\nFeature Coefficients:")
for feature, coefficient in zip(X.columns, model.coef_):
    print(feature, ":", round(coefficient, 2))