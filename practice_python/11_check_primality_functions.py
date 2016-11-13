'''
Ask the user for a number and determine whether the number is prime or not.
'''


def get_int(user_input='Enter a number: '):
    '''
    Gets a string and turns it to integer number.
    '''
    return int(input(user_input))


def is_prime(num):
    '''
    Returns True or False if the number is prime or not.
    '''
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

user_input = get_int('Enter a number to check if its prime: ')

print(is_prime(user_input))
