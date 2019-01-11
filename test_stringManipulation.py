"""
title: tests_stringManipulation
author: sxv3240
date: 1/10/2019 2:42 PM
"""

from string_manipulation import StringManipulation

class Test_string:
    example_one = StringManipulation("Madam,I'm Adam")
    example_two = StringManipulation("howdy")
    example_three = StringManipulation("Third Times The ChArM")

    def test_reversal(self):
        """
        Test for reversal with 3 test cases
        1. Madam, I'm Adam
        2. howdy
        3. Third Times The ChArM
        """
        assert self.example_one.string_reversal() == "Madam,I'm Adam"[::-1]
        assert self.example_two.string_reversal() == "howdy"[::-1]
        assert self.example_three.string_reversal() == "Third Times The ChArM"[::-1]

    def test_removing_case(self):
        """
        Test for removing case with 3 test cases
        1. Madam, I'm Adam
        2. howdy
        3. Third Times The ChArM
        """

        assert self.example_one.removing_case() == "madamimadam"
        assert self.example_two.removing_case() == "howdy"
        assert self.example_three.removing_case() == "thirdtimesthecharm"


    def test_is_vowel(self):
        """
        Test for has vowels with 3 test cases
        1. Madam, I'm Adam
        2. howdy
        3. Third Times The ChArM
        """

        assert self.example_one.is_vowel() ==True
        assert self.example_two.is_vowel() ==True
        assert self.example_three.is_vowel() ==True