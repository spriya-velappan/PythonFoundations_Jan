"""
title: String_Exercise1
author: sxv3240
date: 1/8/2019 10:16 AM
"""
import random
first_name = input("What is your first name?")
last_name = input("What is your last name?")
city_born = input("What is your born city name?")
univ_name = input("Which university you graduated from?")
relative_name = input("What is your relative name?")
friend_name = input("What is your friend name?")

'employee id creation:'

#res_lname =last_name[::-1]
employee_id =first_name[:3] + last_name[-2:]
print("employee_id:" ,employee_id)

'User id creation'
res_univ =univ_name[::-1]
user_id =city_born[:2] + res_univ[:3]
print("user_id:",user_id)

'password creation'
relative_rnd = random.randint(0,len(relative_name)-1)
friend_rnd = random.randint(1,len(friend_name))
password= relative_name[relative_rnd:]+friend_name[:friend_rnd]
print("password:",password)



