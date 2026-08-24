import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# E-commerce transaction data
data = {
    "Customer_ID": ["C01", "C02", "C03", "C04", "C05",
                    "C06", "C07", "C08", "C09", "C10"],
    "Total_Spent": [500, 700, 900, 2500, 2800,
                    3200, 6000, 6500, 7000, 7500],
    "Items_Purchased": [2, 3, 4, 10, 12,
                        14, 25, 27, 30, 32]
}

df = pd.DataFrame(data)

# Select features
X = df[["Total_Spent", "Items_Purchased"]]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create K-Means model
kmeans = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# Assign clusters
df["Cluster"] = kmeans.fit_predict(X_scaled)

print("Customer Cluster Results:")
print(df)

# Display cluster summary
print("\nCluster Summary:")
print(
    df.groupby("Cluster")[
        ["Total_Spent", "Items_Purchased"]
    ].mean()
)

# Scatter plot
plt.scatter(
    df["Total_Spent"],
    df["Items_Purchased"],
    c=df["Cluster"]
)

plt.xlabel("Total Spent")
plt.ylabel("Items Purchased")
plt.title("Customer Segmentation Using K-Means")
plt.grid(True)

plt.show()