import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import StandardScaler

# Customer dataset
data = {
    "Usage_Minutes": [100, 150, 200, 250, 300,
                      350, 400, 450, 500, 550],
    "Contract_Months": [24, 24, 18, 18, 12,
                        12, 6, 6, 3, 3],
    "Churn": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Usage_Minutes", "Contract_Months"]]
y = df["Churn"]

# Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Train logistic regression
model = LogisticRegression()
model.fit(X_scaled, y)

# User input
usage = float(input("Enter usage minutes: "))
contract = int(input("Enter contract duration in months: "))

new_customer = [[usage, contract]]
new_customer = scaler.transform(new_customer)

# Prediction
prediction = model.predict(new_customer)

if prediction[0] == 1:
    print("\nPrediction: Customer will churn")
else:
    print("\nPrediction: Customer will not churn")