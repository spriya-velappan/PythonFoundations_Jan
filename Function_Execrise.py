"""
title: Function_Execrise
author: sxv3240
date: 1/8/2019 1:49 PM
"""

def age_calculator(year1,year2):
    diff_btw=(year1-year2)
    return diff_btw

print(age_calculator(year1=2018,year2=1900))


def avg_numbers(a,b,c):
    avg_nbr =(a+b+c)/3
    return avg_nbr

print(avg_numbers(a=4,b=7,c=8))


def avg_numbers(*args):
    return(args[0]+args[1]+args[2])/args.__len__()

print(avg_numbers(4,7,8))
