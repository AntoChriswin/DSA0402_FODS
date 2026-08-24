import pandas as pd
from sklearn.tree import DecisionTreeRegressor

# Create car dataset
data = {
    "Mileage": [15000, 25000, 40000, 50000, 60000,
                75000, 90000, 100000, 120000, 140000],
    "Age": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Brand": [1, 1, 2, 2, 1, 3, 2, 3, 1, 3],
    "Engine": [2, 2, 1, 2, 1, 1, 2, 1, 1, 2],
    "Price": [25000, 23000, 21000, 19000, 17000,
              15000, 13000, 11000, 9000, 7000]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Mileage", "Age", "Brand", "Engine"]]
y = df["Price"]

# Create CART regression model
model = DecisionTreeRegressor(random_state=42, max_depth=4)

# Train model
model.fit(X, y)

# User input
mileage = float(input("Enter mileage: "))
age = float(input("Enter car age: "))
brand = int(input("Enter brand code (1/2/3): "))
engine = int(input("Enter engine code (1/2): "))

new_car = pd.DataFrame({
    "Mileage": [mileage],
    "Age": [age],
    "Brand": [brand],
    "Engine": [engine]
})

# Predict price
prediction = model.predict(new_car)[0]

print("\nPredicted Car Price:", round(prediction, 2))

# Display decision path
node_indicator = model.decision_path(new_car)
leaf_id = model.apply(new_car)[0]

tree = model.tree_

print("\nDecision Path:")

for node_id in node_indicator.indices:
    if node_id == leaf_id:
        print("Reached prediction leaf node:", node_id)
        break

    feature_index = tree.feature[node_id]
    threshold = tree.threshold[node_id]

    feature_name = X.columns[feature_index]
    value = new_car.iloc[0, feature_index]

    if value <= threshold:
        print(
            f"{feature_name} <= {threshold:.2f}"
        )
    else:
        print(
            f"{feature_name} > {threshold:.2f}"
        )