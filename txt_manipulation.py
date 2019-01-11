"""
title: txt_manipulation
author: sxv3240
date: 1/9/2019 3:19 PM
"""

def read_lines():
    with open('names.txt', 'r') as names_file:
        names = names_file.read().splitlines()

    vowels = "aeiouAEIOU"
    vowels = sorted(set(vowels))

    num_lines = len(names)

    for i in range(num_lines):
        name = names[i]

        if name[0] in (vowels):
            names[i] = names[i] + " Phillips\n"
        else:
            names[i] = names[i] + " Moses\n"

    print(names)

    with open('names.txt', 'w') as new_names:
        new_names.write("Firstname Lastname\n")
        new_names.writelines(names)

def main():
    # dice()
     read_lines()


if __name__ == '__main__':
    print("Called From:", __name__)

    main()