import pandas as pd

# Sample sales data
data = {
    'product_name': ['Laptop', 'Mouse', 'Keyboard', 'Laptop', 'Mouse',
                     'Monitor', 'Laptop', 'Keyboard', 'Mouse', 'Monitor'],
    'quantity_sold': [5, 10, 7, 8, 12, 6, 9, 5, 15, 4]
}

df = pd.DataFrame(data)

# Find top 5 products
top_5 = df.groupby('product_name')['quantity_sold'].sum() \
          .sort_values(ascending=False) \
          .head(5)

print("Top 5 Most Sold Products:")
print(top_5)