"""
title: string_manipulation.py
author: sxv3240
date: 1/10/2019 1:29 PM
"""

class StringManipulation:
    """
    Creation of class to manipulation string
    """

    def __init__(self, altering_str):
        print("This is the constructor method")
        self.altering_str = altering_str

    def string_reversal(self,reserve=None):
       if reserve == None:
        return self.altering_str[::-1]
       else:
        return reserve[::-1]

    def removing_case(self,removed=None):
        if removed == None:
            removed=self.altering_str
        for symbol in "?,.! -_'":
            removed =removed.replace(symbol,"")
        else:
            return removed.lower()

    def is_vowel(self,searching=None):
        if searching is None:
            searching =self.altering_str
        return bool(set(searching).intersection("AEIOUaeiou"))

    def is_palindrome(self, reverse=None):
        reverse = self.string_reversal(reverse)
        reverse = self.removing_case(reverse)
        return reverse[::-1] == reverse

    def __str__(self):
        return f"""String reversed: {self.string_reversal()}
        String cases removed: {self.removing_case()}
        String has vowel: {self.is_vowel()}
        String is palindrome: {self.is_palindrome()}"""

if __name__ == "__main__":
        example_one = StringManipulation("Madam, I'm Adam")
        print(example_one)
        print("=" * 40)
        second_example = StringManipulation("howdy")
        print(second_example)
        print("=" * 40)
        example_three = StringManipulation("Third Times The ChArM")
        print(example_three)
        print(example_one.string_reversal("toast"))



