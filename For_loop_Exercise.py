"""
title: For_loop_Exercise
author: sxv3240
date: 1/9/2019 11:09 AM
"""


def create_string():
    letters = ['O', 'r', 'a', 'n', 'g', 'e', ' ', 'M', 'e', 't', 'h', 'o', 'd']

    for i in letters:
         print(i, end='')


def fill_ticket():
 list =[]

 for i in range(5):
     number = int(input('Enter a number:'))
     list.insert(i, number)
 return list


def matches(guesses, winners):
    temp = 0
    for i in range(5):
       if guesses[i] == winners[i]:
        temp += 1
    return temp

def caesar_cipher(string):
    caesar=""
    cipher_key = {'a': 'n', 'b': 'o', 'c': 'p', 'd': 'q', 'e': 'r', 'f': 's', 'g': 't', 'h': 'u', 'i': 'v', 'j': 'w',
                  'k': 'x', 'l': 'y', 'm': 'z', 'n': 'a', 'o': 'b', 'p': 'c', 'q': 'd', 'r': 'e', 's': 'f', 't': 'g',
                  'u': 'h', 'v': 'i', 'w': 'j', 'x': 'k', 'y': 'l', 'z': 'm'}

    for i in string:
       caesar+=cipher_key.get(i,i)
    return caesar



def main():
    #create_string()
    guesses = fill_ticket()
    winners = [1, 2, 3, 4, 5]
    print(matches(guesses, winners))
    print(guesses)
    print(caesar_cipher("pnrfne pvcure? v zhpu cersre pnrfne fnynq!"))








if __name__ == '__main__':
    print("Called From:", __name__)

    main()