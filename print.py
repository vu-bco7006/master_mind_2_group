"""
# To open the pc.json file and print to screen

import json

file_pc = open("pc.json", "r")

try:
    file_content = file_pc.read()
    data_file_pc = json.loads(file_content)
    print(data_file_pc)

    print("\n")

finally:
    file_pc.close()"""

"""
# To open the csv files and print to screen

import csv

file_orders = open("orders.csv", "r")
file_order_details = open("order_details.csv", "r")

try:
    csv_reader_file_orders = csv.reader(file_orders)
    line_count = 0
    for row in csv_reader_file_orders:
        if line_count == 0:
            print("Column names are: ", row[0], row[1], row[2], row[8])
        else:
            print("Order ID:", row[0], "Customer:", row[1], "Freight:", row[2], "Country:", row[8])
        line_count += 1

    print("\n")

    csv_reader_file_order_details = csv.reader(file_order_details)
    # line_count = 0
    for row in csv_reader_file_order_details:
        if line_count == 0:
            print("Column names are: ", row[0], row[2], row[3], row[4])
        else:
            print("Order ID:", row[0], "Product Category ID:", row[2], "Unit Price:", row[3], "Quantity:", row[4])
        line_count += 1

finally:
    file_orders.close()
    file_order_details.close()
"""

# To import using pandas and numpy

import pandas as pd
import numpy as np

frame_pc = pd.read_json("pc.json")
print(f'This is file pc.json : \n \n {frame_pc} \n')

frame_orders = pd.read_csv("orders.csv")
print(f'This is file orders.csv : \n \n {frame_orders} \n')

frame_order_details = pd.read_csv("order_details.csv")
print(f'This is file order_details.csv : \n \n {frame_order_details} \n')

# Questions 1 - To calculate the freight costs in July 2021

freight_costs = frame_orders['freight']

# print(f'This is the column of freight costs: \n \n {freight_costs} \n')

print(f'Question 1 - The freight costs in July 2021 is ($): {freight_costs.sum()} \n')

# Question 2 - To find the countries with the most orders

country_count = frame_orders['ship_country'].value_counts()
# print(country_count)

print(f'Question 2 - The 5 countries with the highest number of orders in July 2021: \n{country_count}\n')

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
3.  Obtain the highest revenue amount using NumPy's 'max' function, then select it's product category by filtering in pandas.
4.  Select the "category_name" in 'pc.json' for the product category with the highest revenue amount. 
"""

# Step 1:

a = frame_order_details['unit_price']
b = frame_order_details['quantity']
frame_order_details['total_cost'] = a * b  # 'total_cost' is a new variables in frame_order_details

# print(a, b)

# print(frame_order_details['total_cost'])

# Step 2:

product_category_id_revenue = frame_order_details[['product_category_id', 'total_cost']].groupby(['product_category_id']).sum()
print(product_category_id_revenue)

# Step 3:

highest_revenue_amount = product_category_id_revenue['total_cost'].max()  # 'highest_revenue_amount' is a new variable
x = product_category_id_revenue[product_category_id_revenue['total_cost'] == highest_revenue_amount]  # filtering
print(f'\n{x}\n')

# step 4:

# print(product_category_id_revenue['product_category_id'])

for j, k in frame_pc.items():  # refer to lecture 7 and workshop codes in Python for selecting 'product_name' with 'category_id' == x['product_category_id']
    print(j, k)

# y = frame_pc.get("category_id", "1")
# print(y)
