"""
title: Error_Catch_Pratice
author: sxv3240
date: 1/7/2019 2:36 PM
"""

# try:
#     print(4 +spam +4)
#
# except NameError as error:
#     print("Hey,that's not cool!", error)
#
#     try:
#         print("2" + spam + 15)
#     except (NameError, TypeError):
#         print("Very sorry, we are unable to evaluate your request. Please correct errors and re-evaluate.")
#
#     try:
#         print("2" + spam + 15)
#     except TypeError as e:
#         print("You gave the wrong type there buddy!", e)
#     except NameError as e:
#         print("That variable name does not exist!", e)



try:
    eval('x===x')
except SyntaxError as e:
    print("Very sorry, we are unable to evaluate your request. Please correct errors and re-evaluate.", e)

try:
    print(10/0)
except ZeroDivisionError as e:
    print(e)

try:
    print(4 + spam)
except (NameError, TypeError):
    print("Very sorry, we are unable to evaluate your request. Please correct errors and re-evaluate.")

try:
    print(2+"2")
    raise TypeError
except TypeError as e:
        print("Hello",e)







