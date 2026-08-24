import matplotlib.pyplot as plt

# Monthly temperature data
months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]

temperature = [24, 26, 29, 32, 34, 33, 31, 30, 29, 28, 26, 24]

# Create line plot
plt.plot(months, temperature, marker='o')

plt.title("Monthly Temperature")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.grid(True)

plt.show()

plt.scatter(months, temperature, color='red')
plt.title("Monthly Temperature Scatter Plot")
plt.xlabel("Month")
plt.ylabel("Temperature (°C)")
plt.show()
