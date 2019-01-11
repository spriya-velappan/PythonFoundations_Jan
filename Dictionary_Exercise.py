"""
title: Dictionary_Exercise
author: sxv3240
date: 1/9/2019 10:00 AM
"""

#methods added to test call from other file


def home():
    print("from main")


if __name__ != '__main__':
    print("Called From:", __name__)

    home()


#mycode
def polling_friends():
    fav_animals ={'Gordo':'Dog','Miranda':'Cat'}
    person = input('what is your name?')
    print(f'{person},what is your favorite animal?',fav_animals[person])



polling_friends()


#Solution:


def polling_friends():
    fav_animals = {}
    key1 = input("Enter your name: ")
    value1 = input("Enter your favorite animal: ")
    key2 = input("Enter your name: ")
    value2 = input("Enter your favorite animal: ")
    fav_animals[key1] = value1
    fav_animals[key2] = value2
    return fav_animals


# Call (invoke) the function like shown below:
print(polling_friends())


#Birthday_month


