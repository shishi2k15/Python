"""
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will
turn 100 years old.
"""

from datetime import date

current_year = int(date.today().year)

name = input('Enter your name please: ')
age = int(input('Enter your age: '))
user_birthday = current_year - age

year = str(user_birthday + 100)


print(name + " will be 100 years old in the year of " + year)
