'''
Write a program (function!) that takes a list and returns a new list that
contains all the elements of the first list minus all the duplicates.
'''
num_list = [1, 2, 3, 3, 3, 2, 5, 3, 4, 4]


def dup_rem_loop(x):
    y = []
    y = [i for i in x if i not in y]
    return y


def dup_remove(a_list):
    return set(a_list)

print(dup_remove(num_list))
print(dup_remove(num_list))
