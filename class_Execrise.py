"""
title: class_Execrise
author: sxv3240
date: 1/10/2019 12:56 PM
"""

class Player:
        """
        Creates a game Player template.
        """

        def __init__(self, user_name,points=0):
            print("This is the constructor method")
            self.user_name = user_name
            self.points = points

        def gain_point(self, points):
            """Prints that the user has gained a certain number of points."""
            self.points += points
            print(f"Yay! You have gained {points} point(s)! That means you now have {self.points} points!")

        def lose_point(self, points):
            """Prints that the user has lost a certain number of points."""
            self.points -= points
            print(f"Oh no! You have lost {points} point(s)! That means you now have {self.points} points!")

def main():
        ralph = Player("R@!ph123", 100)
        ralph.gain_point(10)
        ralph.lose_point(5)

if __name__ == "__main__":
        main()