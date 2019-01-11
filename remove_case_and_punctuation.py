"""
title: remove_case_and_punctuation
author: sxv3240
date: 1/8/2019 11:24 AM
"""


"""
Create a program that has the user enter a string of any length. Change the case of every letter to lower case and remove all of the occurrences of symbols and spaces.

Example Output:

>>> Enter a phrase: Madam, I'm Adam
madamimadam
"""

# import re
# #user_string = "Hi! this is sunny @@@"
# # user_string = "Madam, I'm Adam"
# user_string = input("Enter a phrase: ")
# string_split = user_string.lower().split()
# string_rejoin = "".join(re.findall("[a-z]", "".join(string_split)))
# print(string_rejoin)
#
# print("Palindrome?" ,string_rejoin ==string_rejoin[::-1])


def has_vowel(word):
    # Check whether name has a vowel
    if set('aeiou').intersection(word.lower()):
        print(word, 'contains a vowel.')
    else:
        print(word, 'does not contain a vowel.')

has_vowel("supercalifragilisticexpialidocious")
has_vowel("why")
has_vowel("hey")