import pandas as pd

order_data = pd.DataFrame({
    'Customer_ID': [101, 102, 101, 103, 102],
    'Order_Date': ['2026-01-10', '2026-01-12', '2026-02-05',
                   '2026-02-15', '2026-03-01'],
    'Product_Name': ['Laptop', 'Mouse', 'Mouse', 'Laptop', 'Mouse'],
    'Order_Quantity': [1, 2, 3, 2, 1]
})

# Convert order date to datetime
order_data['Order_Date'] = pd.to_datetime(order_data['Order_Date'])

# 1. Total number of orders by each customer
total_orders = order_data.groupby('Customer_ID').size()

# 2. Average order quantity for each product
average_quantity = order_data.groupby('Product_Name')['Order_Quantity'].mean()

# 3. Earliest and latest order dates
earliest_date = order_data['Order_Date'].min()
latest_date = order_data['Order_Date'].max()

print("Total Orders by Each Customer:")
print(total_orders)

print("\nAverage Order Quantity for Each Product:")
print(average_quantity)

print("\nEarliest Order Date:", earliest_date.date())
print("Latest Order Date:", latest_date.date())