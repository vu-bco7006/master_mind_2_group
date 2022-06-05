# Importing pandas and numpy into Python:

import pandas as pd
import numpy as np

# Importing files:

frame_pc = pd.read_json("pc.json")
# print(f'This is file pc.json : \n \n {frame_pc} \n')

frame_orders = pd.read_csv("orders.csv")
# print(f'This is file orders.csv : \n \n {frame_orders} \n')

frame_order_details = pd.read_csv("order_details.csv")
# print(f'This is file order_details.csv : \n \n {frame_order_details} \n')

# Questions 1 - To calculate the freight costs in July 2021

freight_costs = frame_orders['freight']

# print(f'This is the column of freight costs: \n \n {freight_costs} \n')

print(f'Question 1 - The freight costs in July 2021 is ($): {freight_costs.sum()} \n')

# Question 2 - To find the countries with the most orders

country_count = frame_orders['ship_country'].value_counts()
# print(country_count)

print(f'Question 2 - The 2 countries with the highest number of orders in July 2021: \n{country_count.head(2)}\n')

""" 
# Alternative options for obtaining the solution (2 examples):

for name, group in frame_orders.groupby('ship_country'):
    print(name)
    print(group)

for name in frame_orders['ship_country']:
    print(name)
"""

# Question 3 - To find the 3 customers with the highest number of orders

customer_name_count = frame_orders['customer_name'].value_counts()
# print(f'The number of orders per customer in July 2021 is: \n{customer_name_count}\n')

print(f'Question 3 - The 3 customers with the highest number of orders in July 2021: \n{customer_name_count.head(3)}\n')

# Question 4 - To find the product category with the highest sales revenue

"""
Steps - In data file 'order_details.csv':
1.  The total cost per order is calculated as -
        total_cost = unit_price x quantity,
        total_cost will be a new variable (column).
2.  Use the Pandas 'groupby' function to obtain product_category_id revenue for July 2021.
3.  Adding a key with values (as a list) to the list of dictionaries in 'frame_pc.json'.
4.  Obtain the highest revenue amount using NumPy's 'max' function.
5.  Select the item with maximum value from within the list of dictionaries.
6.  Print as output the product category name with the maximum revenue.
"""

# Step 1:

a = frame_order_details['unit_price']
b = frame_order_details['quantity']
frame_order_details['total_cost'] = a * b  # 'total_cost' is a new variables in frame_order_details
# print(frame_order_details['total_cost'])

# Step 2 - Obtaining sum of total cost for orders by 'category_id':

product_category_rev = frame_order_details[['product_category_id', 'total_cost']].groupby(['product_category_id']).sum()
# print(product_category_rev)

# Step 3 - Adding a key and values (as a list) to list of dictionaries in 'frame_pc.json':

product_category_revenue = list(product_category_rev['total_cost'])  # need to check if this should be a tuple or list
# print(product_category_revenue)

product_category_revenue = [int(q) for q in product_category_revenue]  # convert to a list of integers
# print(product_category_revenue)

frame_pc['product_revenue'] = product_category_revenue
# print(f'This is the list of dictionaries with "product_revenue" column: \n{frame_pc}')

frame_pc["category_id"] = [int(s) for s in frame_pc["category_id"]]  # delete this line if not required
frame_pc["category_name"] = list(frame_pc["category_name"])  # delete this line if not required


# Step 4 - Obtaining the product category with the highest revenue in July 2021:

highest_revenue_amount = product_category_rev['total_cost'].max()  # 'highest_revenue_amount' is a new variable
x = product_category_rev[product_category_rev['total_cost'] == highest_revenue_amount]  # filtering
# print(f'\n{x}\n')

p = ()

for j, k in x.items():
    p = int(k)  # variable 'k' is the revenue amount (integer) for the product category that has the highest revenue

# print(p)

# step 5 - Select the item with maximum value from within the list of dictionaries 'product_category_revenue':

for i in frame_pc.items():
    if i["total_cost"] == 'p':
        frame_pc = i
        print(i)
        print(f"{frame_pc['category_name']} contributed to the highest revenue of {frame_pc['total_cost']}.")

