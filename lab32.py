import pandas as pd
from sklearn.linear_model import LinearRegression

# Housing dataset
data = {
    "Area": [1000, 1200, 1500, 1800, 2000, 2200, 2500, 2800],
    "Bedrooms": [2, 2, 3, 3, 4, 4, 5, 5],
    "Price": [200000, 240000, 300000, 360000,
              400000, 440000, 500000, 560000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Area", "Bedrooms"]]
y = df["Price"]

# Create and train model
model = LinearRegression()
model.fit(X, y)

# User input
area = float(input("Enter house area: "))
bedrooms = int(input("Enter number of bedrooms: "))

# Prediction
new_house = [[area, bedrooms]]
predicted_price = model.predict(new_house)

print("\nPredicted House Price:",
      round(predicted_price[0], 2))