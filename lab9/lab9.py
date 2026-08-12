import pandas as pd


property_data = pd.DataFrame({
    "Property ID": [101, 102, 103, 104, 105],
    "Location": ["Chennai", "Bangalore", "Chennai", "Hyderabad", "Bangalore"],
    "Bedrooms": [3, 5, 4, 6, 5],
    "Area (sq ft)": [1500, 2200, 1800, 3000, 2500],
    "Listing Price": [5000000, 8500000, 6200000, 12000000, 9000000]
})

avg_price = property_data.groupby("Location")["Listing Price"].mean()

count_bedrooms = len(property_data[property_data["Bedrooms"] > 4])

largest_property = property_data.loc[property_data["Area (sq ft)"].idxmax()]

print("Average Listing Price by Location:")
print(avg_price)

print("\nNumber of Properties with More Than 4 Bedrooms:")
print(count_bedrooms)

print("\nProperty with the Largest Area:")
print(largest_property)
