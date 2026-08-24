import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Customer dataset
data = {
    "Age": [20, 22, 25, 28, 45, 48, 50, 52, 60, 62],
    "Annual_Spending": [1000, 1200, 1500, 1800, 5000,
                        5500, 6000, 6500, 9000, 9500],
    "Purchases": [5, 6, 7, 8, 20, 22, 24, 25, 35, 38]
}

df = pd.DataFrame(data)

# Select features
X = df[["Age", "Annual_Spending", "Purchases"]]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

# Assign clusters
df["Cluster"] = kmeans.fit_predict(X_scaled)

print("Customer Segments:")
print(df)

# Visualize clusters
plt.scatter(
    df["Annual_Spending"],
    df["Purchases"],
    c=df["Cluster"]
)

plt.xlabel("Annual Spending")
plt.ylabel("Number of Purchases")
plt.title("Customer Segmentation")
plt.show()