import numpy as np

# Item prices and quantities
prices = np.array([100, 50, 200])
quantities = np.array([2, 3, 1])

# Discount and tax rates
discount_rate = 10
tax_rate = 5

# Calculate subtotal
subtotal = np.sum(prices * quantities)

# Calculate discount
discount = subtotal * discount_rate / 100
amount_after_discount = subtotal - discount

# Calculate tax
tax = amount_after_discount * tax_rate / 100

# Calculate final total cost
total_cost = amount_after_discount + tax

# Display results
print("Subtotal:", subtotal)
print("Discount Amount:", discount)
print("Amount After Discount:", amount_after_discount)
print("Tax Amount:", tax)
print("Final Total Cost:", total_cost)