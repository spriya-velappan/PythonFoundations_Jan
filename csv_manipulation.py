"""
title: csv_manipulation.py
author: sxv3240
date: 1/10/2019 8:49 AM
"""

import csv

#
#with open('addresses.csv', 'r') as address_data:
#     read_address_data = list(csv.reader(address_data))
#     print(read_address_data)
#    print(list(read_address_data))
#
#     print(read_address_data[3][1])
#    #n order for Python to give us a neat list of our data for us to manipulate,
#     # cast the the read_address_data variable with list() and print it out.
#     list_address_data=list(read_address_data)
#     for i, row in enumerate(list_address_data):
#         print(f"Row #: {i} {row}")
#
#         #modifying
#         # Changing row 2’s values
#         list_address_data[2] = ['Reese', 'Witherspoon', '362 Main St', 'Austin', 'TX', '78704']
#         #Changing row 3, column 1’s  value
#         list_address_data[3][0] = 'Elizabeth'


        # with open('addresses.csv', 'w') as address_data_file:
        #     write_address_data = csv.writer(address_data_file)
        #     write_address_data.writerows(list_address_data)
        #
        #     write_address_data.writerow(['Alegra', 'Cole', '1 Broadway Rd', 'New York City', 'NY', 15432])


        # with open('addresses.csv', 'r') as address_data:
        #     reader = csv.DictReader(address_data)
        #     headers = reader.fieldnames
        #     addresses = list(reader)
        #     print(headers,"\n",addresses)
        #     print("\n\n\n")
        #
        #     for row in addresses:
        #         del row["Address Line"]
        #
        #     print(addresses)
        #
        #     headers.remove("Address Line")
        #
        #     with open('addresses_altered.csv', 'w') as address_data:
        #         writer = csv.DictWriter(address_data, fieldnames=headers)
        #         writer.writeheader()
        #         writer.writerows(addresses)


#with open('SalesJan2009.csv', 'r') as salesJan_data:
   #  read_sales_data = list(csv.reader(salesJan_data))
   # # print(read_sales_data)
   #  #print(list(read_sales_data))
   #
   #  num_of_lines = len(read_sales_data)
   #  print(num_of_lines)

with open('SalesJan2009.csv', 'r') as salesJan_data:
        reader = csv.DictReader(salesJan_data)
        headers = reader.fieldnames
        addresses = list(reader)
        num_of_lines =len(addresses)
        print(num_of_lines)
        for row in addresses:
             print(row["Latitude"], row["Longitude"])

        headers.append("distance")
        headers.append("potential_friend")
        print(headers)




#Class Solution
import math
import csv

with open('SalesJan2009.csv') as sales_file:
    list_sales_data = csv.DictReader(sales_file)
    headers = list_sales_data.fieldnames
    list_sales_data = list(list_sales_data)
    print(len(list_sales_data))
    final_output = []
    for i, line in enumerate(list_sales_data, 1):
        line = dict(line)
        final_output.append(line)
        diff_lat = round(abs(float(line['Latitude']) - 30.2672), 2)
        diff_long = round(abs(float(line['Longitude']) - 97.7431), 2)
        print( f"Transaction #{i:0>3}: {diff_lat:>6} {diff_long:>6}" )
        print(type(headers))

headers.extend(['Distance', 'Potential Friends'])

def dist_form(lat1, long1, lat2, long2):
    return math.sqrt((lat1 - lat2)**2 + (long1 - long2)**2)

for i, row in enumerate(final_output):
    distance = dist_form(float(row['Latitude']), float(row['Longitude']), 30.2672, 97.7431)
    final_output[i]['Distance'] = distance
    final_output[i]['Potential Friends'] = distance < 100

with open('sales_and_friends.csv', 'w') as sales_data:
    writer = csv.DictWriter(sales_data, fieldnames=headers)
    #print(headers)
    writer.writeheader()
    writer.writerows(final_output)






