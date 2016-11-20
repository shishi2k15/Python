'''
Write a password generator in Python. Be creative with how you generate
passwords - strong passwords have a mix of lowercase letters, uppercase
letters, numbers, and symbols. The passwords should be random, generating
a new password every time the user asks for a new password. Include your
run-time code in a main method.
'''
import random


def pass_gen(pass_len):
    """
    Generates random passowrd with given lenght.
    """
    s = "abcdefghijklmnopqrstuvwxyz012345678\
        90ABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()?"

    password = ''.join(random.sample(s, pass_len))
    return password

user_lenght_choice = int(input('How long password would you like ?\n'))
print pass_gen(user_lenght_choice)
