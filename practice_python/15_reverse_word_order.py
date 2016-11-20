'''
Write a program (using functions!) that asks the user for a long string
containing multiple words. Print back to the user the same string,
except with the words in backwards order.
'''


# def reverse_order(input_list):
#     """
#     Takes the input list and returns it in reverse order.
#     """
#     return input_list[::-1]


# def string_list(input_string):
#     """
#     Converts a string into list of words.
#     """
#     input_string = input_string.split(' ')
#     return input_string

# Really short (but not so readable) version
def reverse_string(word):
    return ' '.join(word.split()[::-1])


user_input = str(raw_input('Enter a string to be reversed: '))
print(reverse_string(user_input))
