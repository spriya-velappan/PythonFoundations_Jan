"""
title: List_Tuple_Exercise
author: sxv3240
date: 1/8/2019 3:11 PM
"""
import random
def shake_ball():
    list = ["Yes definitely", "As I see it", "yes",
            "Ask again later", "Cannot predict now",
            "Don’t count on it", "Very doubtful"]

    # return_value = list(random.randint(1,len(list)-1))
    return_value = random.choice(list)
    return return_value

question =input("Ask a question:")
print(shake_ball())


def gymnast_scores():
    list2 = ["1","2","3","4","5"]

    print(f"The lowest possible score is {min(list2)},and he lowest possible score is {max(list2)}")

    print(f"A judge can give a gymnast {random.choice(list2)} points")

gymnast_scores()
