import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Dataset
data = {
    "Size": [1000, 1200, 1400, 1600, 1800,
             2000, 2200, 2400, 2600, 2800],
    "Price": [200000, 240000, 280000, 320000, 360000,
              400000, 440000, 480000, 520000, 560000]
}

df = pd.DataFrame(data)

# Bivariate scatter plot
plt.scatter(df["Size"], df["Price"])
plt.xlabel("House Size")
plt.ylabel("House Price")
plt.title("House Size vs House Price")
plt.grid(True)
plt.show()

# Features and target
X = df[["Size"]]
y = df["Price"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Train linear regression model
model = LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print("Mean Squared Error:", round(mse, 2))
print("R2 Score:", round(r2, 2))
print("Coefficient:", round(model.coef_[0], 2))