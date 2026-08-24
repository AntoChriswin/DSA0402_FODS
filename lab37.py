import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer purchasing data
data = {
    "Annual_Spending": [1000, 1200, 1500, 5000, 5500,
                        6000, 10000, 11000, 12000],
    "Purchase_Frequency": [5, 6, 7, 20, 22, 25, 40, 42, 45]
}

df = pd.DataFrame(data)

X = df[["Annual_Spending", "Purchase_Frequency"]]

# Scale data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
kmeans.fit(X_scaled)

# User input
spending = float(input("Enter annual spending: "))
frequency = float(input("Enter purchase frequency: "))

new_customer = scaler.transform([[spending, frequency]])

# Predict cluster
cluster = kmeans.predict(new_customer)

print("\nCustomer belongs to Segment:", cluster[0])