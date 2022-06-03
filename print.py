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

print(f'This is the column of freight costs: \n \n {freight_costs} \n')

print(f'The freight costs in July 2021 were ($): {freight_costs.sum()} \n')

# Question 2 - To find the countries with the most orders

# country = frame_orders['ship_country']

# print(f'This is the country using header function with max 60: \n \n{country_sort.head(60)}')
# print(f'This is the country using describe function: \n \n{country_sort.describe}')

# print(f'This is the column of countries: \n \n{country} \n')

# print(f'The sort by country is: \n \n{country_sort} \n')

for name, group in frame_orders.groupby('ship_country'):  # perhaps need to use if/then function to restrict to n>=20 rows (eg Germany & USA)
    print(name)
    print(group)

for name in frame_orders['ship_country']:
    print(name)




# doesn't work as string variable:  print(f'The count of country for shipping: {country.sum()} \n')
# print(country.groupby(['ship_country']))

