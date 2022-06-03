# To open the pc.json file and print to screen

import json

file_pc = open("pc.json", "r")

try:
    file_content = file_pc.read()
    data = json.loads(file_content)
    print(data)

    print("\n")

finally:
    file_pc.close()

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


