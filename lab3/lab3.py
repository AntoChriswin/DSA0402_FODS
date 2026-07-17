import numpy as np

# Load the dataset
house_data = np.genfromtxt("houses.csv", delimiter=",", skip_header=1)

# Select houses with more than 4 bedrooms
filtered_data = house_data[house_data[:, 0] > 4]

# Calculate average sale price
average_price = np.mean(filtered_data[:, 2])

# Display result
print("Average Sale Price:", average_price)