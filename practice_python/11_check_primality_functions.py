'''
Ask the user for a number and determine whether the number is prime or not.
'''


def is_prime(num):
    if num < 2:
        return False
    if num % 2 == 0:
        return num == 2
    div = 3
    while div * div <= num:
        if num % div == 0:
            return False
        div += 2
    return True

user_input = int(input('Enter a number to check if its prime: '))

print(is_prime(user_input))
