import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

# Create the dataset
data = {
    "Age": [23, 23, 27, 27, 39, 41, 47, 49, 50,
            52, 54, 54, 56, 57, 58, 58, 60, 61],

    "Fat": [9.5, 26.5, 7.8, 17.8, 31.4, 25.9, 27.4, 27.2, 31.2,
            34.6, 42.5, 28.8, 33.4, 30.2, 34.1, 32.9, 41.2, 35.7]
}

df = pd.DataFrame(data)

# Display dataset
print("Dataset:")
print(df)

# Calculate mean, median and standard deviation
print("\nMean:")
print(df.mean())

print("\nMedian:")
print(df.median())

print("\nStandard Deviation:")
print(df.std())

# -----------------------------
# Boxplots
# -----------------------------
plt.figure(figsize=(8, 5))
sns.boxplot(data=df)
plt.title("Boxplot of Age and Body Fat")
plt.ylabel("Value")
plt.show()

# -----------------------------
# Scatter Plot
# -----------------------------
plt.figure(figsize=(8, 5))
plt.scatter(df["Age"], df["Fat"])
plt.title("Age vs Body Fat")
plt.xlabel("Age")
plt.ylabel("Body Fat (%)")
plt.grid(True)
plt.show()

# -----------------------------
# Q-Q Plot for Age
# -----------------------------
plt.figure(figsize=(7, 5))
stats.probplot(df["Age"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Age")
plt.show()

# -----------------------------
# Q-Q Plot for Body Fat
# -----------------------------
plt.figure(figsize=(7, 5))
stats.probplot(df["Fat"], dist="norm", plot=plt)
plt.title("Q-Q Plot of Body Fat")
plt.show()