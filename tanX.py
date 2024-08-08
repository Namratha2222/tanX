import pandas as pd

# Load the data from the CSV file
orders = pd.read_csv('orders.csv')

# Convert order_date to datetime
orders['order_date'] = pd.to_datetime(orders['order_date'])

# Extract the month and year from the order_date
orders['month'] = orders['order_date'].dt.to_period('M')

# Compute total revenue per month
monthly_revenue = orders.groupby('month')['product_price'].sum()
print("Total revenue per month:")
print(monthly_revenue)

# Compute total revenue per product
product_revenue = orders.groupby('product_name')['product_price'].sum()
print("\nTotal revenue per product:")
print(product_revenue)

# Compute total revenue per customer
orders['revenue'] = orders['product_price'] * orders['quantity']
customer_revenue = orders.groupby('customer_id')['revenue'].sum()
print("\nTotal revenue per customer:")
print(customer_revenue)

# Sort customers by revenue and get the top 10
top_customers = customer_revenue.sort_values(ascending=False).head(10)
print("\nTop 10 customers by revenue:")
print(top_customers)
