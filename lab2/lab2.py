import numpy as np

# 3x3 matrix (each row represents a different product)
sales = np.array([
    [100, 120, 110],
    [200, 210, 190],
    [150, 160, 170]
])

average_price = np.mean(sales)

print("Average Price:", average_price)
