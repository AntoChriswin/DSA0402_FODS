import pandas as pd

# Create temperature dataset
data = {
    "City": ["Chennai", "Chennai", "Chennai",
             "Delhi", "Delhi", "Delhi",
             "Bangalore", "Bangalore", "Bangalore"],
    "Temperature": [30, 32, 31, 20, 35, 25, 24, 26, 25]
}

df = pd.DataFrame(data)

# 1. Mean temperature for each city
mean_temp = df.groupby("City")["Temperature"].mean()

# 2. Standard deviation for each city
std_temp = df.groupby("City")["Temperature"].std()

# 3. Temperature range for each city
temp_range = df.groupby("City")["Temperature"].agg(
    lambda x: x.max() - x.min()
)

# 4. City with highest temperature range
highest_range_city = temp_range.idxmax()

# City with lowest standard deviation
consistent_city = std_temp.idxmin()

print("Mean Temperature:")
print(mean_temp)

print("\nStandard Deviation:")
print(std_temp)

print("\nTemperature Range:")
print(temp_range)

print("\nCity with Highest Temperature Range:",
      highest_range_city)

print("Most Consistent City:",
      consistent_city)