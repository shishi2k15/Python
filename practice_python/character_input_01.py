from datetime import date

current_year = int(date.today().year)

name = input('Enter your name please: ')
age = int(input('Enter your age: '))
user_birthday = current_year - age

year = str(user_birthday + 100)


print(name + " will be 100 years old in the year of " + year)
