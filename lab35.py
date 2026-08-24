import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)

# Create dataset
data = {
    "Age": [20, 25, 30, 35, 40, 45, 50, 55, 60, 65],
    "Income": [20000, 25000, 30000, 35000, 40000,
               45000, 50000, 55000, 60000, 65000],
    "Purchased": [0, 0, 0, 1, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Ask user for features
features_input = input(
    "Enter feature names separated by comma: "
)

features = [x.strip() for x in features_input.split(",")]

target = input("Enter target variable: ")

X = df[features]
y = df[target]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)

# Train model
model = RandomForestClassifier(random_state=42)
model.fit(X_train, y_train)

# Predictions
y_pred = model.predict(X_test)

# Metrics
print("\nAccuracy :", round(accuracy_score(y_test, y_pred) * 100, 2), "%")
print("Precision:", round(precision_score(y_test, y_pred, zero_division=0) * 100, 2), "%")
print("Recall   :", round(recall_score(y_test, y_pred, zero_division=0) * 100, 2), "%")
print("F1-Score :", round(f1_score(y_test, y_pred, zero_division=0) * 100, 2), "%")