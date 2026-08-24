import pandas as pd

# Customer purchase data
data = {
    "Customer_ID": ["C01", "C02", "C03", "C04", "C05", "C06"],
    "Age": [21, 25, 21, 30, 25, 21]
}

df = pd.DataFrame(data)

# Calculate frequency distribution
age_frequency = df["Age"].value_counts().sort_index()

print("Frequency Distribution of Customer Ages:")
print(age_frequency)