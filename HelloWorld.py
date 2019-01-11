"""
title: HelloWorld
author: sxv3240
date: 1/7/2019 10:09 AM
"""

print ("hello world")

def main():


    with open('test.txt', 'r') as test_file:
        days = test_file.readlines()

    num_lines = len(days)
    for i in range(num_lines):
        days[i] = "Yay! It's " + days[i]

    title = "Days of the Week\n"

    with open('test.txt', 'w') as test_file:
        test_file.write(title)
        test_file.writelines(days)





if __name__ == '__main__':
    print("Called From:", __name__)

    main()