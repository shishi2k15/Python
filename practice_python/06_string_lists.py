"""
Ask the user for a string and print out whether this string is a palindrome
or not. (A palindrome is a string that reads the same forwards and backwards.)
"""

user_input = str(raw_input('Enter a string to check if its palindrome: '))

if user_input == user_input[-1::-1]:
    print('It is a palindrome !')
else:
    print("It's not.")
