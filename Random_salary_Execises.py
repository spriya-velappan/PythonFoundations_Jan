"""
title: Random_salary_Execises
author: sxv3240
date: 1/7/2019 2:05 PM
"""

import random

name = input("What is your name:")
salary = int(input("What is your salary:"))
raise_per = random.randint(0,100)
raise_amount = salary * raise_per//100
new_salary = salary + raise_amount

print(f"""{name},your salary is {salary}.
Your raise is {raise_per}% of {salary}.
{name},your new salary is {new_salary}.
""")