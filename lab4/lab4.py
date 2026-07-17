import numpy as np
sales_data = np.array([50000, 65000, 70000, 80000])
total_sales = np.sum(sales_data)
percentage_sales = ((sales_data[3] - sales_data[0]) / sales_data[0]) * 100
print("Sales Data (Q1, Q2, Q3, Q4):", sales_data)
print("Total Sales for the Year:", total_sales)
print("Percentage Increase from Q1 to Q4:", percentage_sales, "%")