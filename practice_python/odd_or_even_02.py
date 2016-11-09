"""
Ask the user for a number. Depending on whether the number is even or odd,
print out an appropriate message to the user. Hint: how does an even / odd
number react differently when divided by 2?

Extras:

    If the number is a multiple of 4, print out a different message.
    Ask the user for two numbers: one number to check (call it num) and one
    number to divide by (check). If check divides evenly into num, tell that
    to the user. If not, print a different appropriate message.
"""

user_num = int(input('Enter a number: '))
user_check = int(input('Enter a number to divide by: '))

if user_num % 4 == 0:
    print('The number is multiple of 4.')
elif user_num % 2 == 0:
    print('The number is even.')
else:
    print('The number is odd.')

if user_num % user_check == 0:
    print('{} divides evenly by {}'.format(user_num, user_check))
else:
    print('{} does not dived evenly by {}'.format(user_num, user_check))
