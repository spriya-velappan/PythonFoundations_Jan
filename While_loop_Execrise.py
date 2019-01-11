"""
title: While_loop_Execrise
author: sxv3240
date: 1/9/2019 1:53 PM
"""


import matplotlib.pyplot as plt
import random

def dice():

    a = []  # create an empty list
    result =0
    while result < 6:
     x = random.choice([1, 2, 3, 4, 5, 6])  # choose a random choice of either 1, 3 or 10 to a (the list)
    a += [x]
    result+=1
    if x==4:

     plt.hist(a, range=(1, 6), align='right')  # options for aligning are 'mid', 'left', and 'right'
    plt.show()

def guessing_game():
    random_nbr = 0
    number = 5
    while random_nbr < 20:
        guess_nbr =int(input("Guess the number:"))
        random_nbr += 0
        if guess_nbr == number:
            print("Your are the winner")
            random_nbr=20

    return guess_nbr

#Class solution
def guessing_game():
 random_num = random.randint(1, 20)

 while True:
        guess = int(input("Take a guess number btw 1-20 : "))
        if (guess == random_num):
         print(" wow correct guess ....!")
        break
 else:
       print(f'Hint +/- 20 with {(20 - random_num)}')


def account_amt():
    total = int(input("Enter the amount :"))
    try:
        while True:
            spent_amt =int(input("Enter Amount Spent: "))
            total -= spent_amt
            print(f"Amount balance:",total)
            if (total<=0):
                print("All out of Money")
                print("Amount has no enough money to spend")
            raise Exception("Out of money")
    except Exception as e:
        print("Out of money")

    return total




def main():
    # dice()
    # guessing_game()

    print(account_amt())


if __name__ == '__main__':
    print("Called From:", __name__)

    main()