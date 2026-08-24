import pandas as pd
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

# Transaction data
data = {
    "Customer_ID": ["C01", "C02", "C03", "C04", "C05",
                    "C06", "C07", "C08", "C09"],
    "Total_Spent": [500, 700, 800, 3000, 3500,
                    4000, 8000, 8500, 9000],
    "Visit_Frequency": [5, 6, 7, 15, 17, 18, 30, 32, 35]
}

df = pd.DataFrame(data)

# Features
X = df[["Total_Spent", "Visit_Frequency"]]

# Standardize
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)

df["Segment"] = kmeans.fit_predict(X_scaled)

print("Customer Segments:")
print(df)

# Analyze segment means
print("\nSegment Summary:")
print(
    df.groupby("Segment")[["Total_Spent", "Visit_Frequency"]].mean()
)