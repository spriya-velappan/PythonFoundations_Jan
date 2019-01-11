"""
title: Sets_Execrise
author: sxv3240
date: 1/9/2019 8:51 AM
"""

# myset1 = set(["Software Engineer", "Sr. Software Engineer",
#               "Staff Software Engineer", "Software Engineer Principal", "Software Engineer"])
# print(myset1)
#
# #The method set1.intersection(set2) will find the similar elements in both set1 and set2.
# jos_favs = {'python', 'c++', 'javascript'}
# als_favs = {'c#', 'python'}
# print(jos_favs.intersection(als_favs))
#
# #Difference
#
# #The method set1.difference(set2) will find the elements in set1 and set2 that are different.
#
# jos_favs = {'python', 'c++', 'javascript'}
# als_favs = {'c#', 'python'}
# print(jos_favs.difference(als_favs))


def remove_duplicates(iterable):
    myset= set(iterable)
    return print(myset)

remove_duplicates('MISSISSIPPI')

def finding_vowels(string):
    if set("aeiou").intersection(string.lower()):
     return True
    else:
     return False


print(finding_vowels('mississippi'))