import matplotlib.pyplot as plt

# Monthly sales data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun"]
sales = [10000, 12000, 15000, 13000, 18000, 20000]

# Create line plot
plt.plot(months, sales, marker='o')

plt.title("Monthly Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.grid(True)

plt.show()

plt.bar(months, sales, color='skyblue')
plt.title("Monthly Product Sales")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

plt.scatter(sales, months, color='green')
plt.title("Sales Scatter Plot")
plt.xlabel("Sales")
plt.ylabel("Month")
plt.show()