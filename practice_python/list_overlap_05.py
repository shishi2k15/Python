"""
Take two lists, say for example these two:

  a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
  b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

and write a program that returns a list that contains only the elements that
are common between the lists (without duplicates). Make sure your program
works on two lists of different sizes.

Extras:

1. Randomly generate two lists to test this
2. Write this in one line of Python code
"""
import random

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

a = range(0, random.randint(0, 21))
b = range(0, random.randint(0, 21))

new_list = []
count = 0

# for x in a:
#    if x in b:
#        new_list.append(x)

new_list = [x for x in a if x in b]
print(set(new_list))
