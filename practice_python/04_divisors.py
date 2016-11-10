"""
Create a program that asks the user for a number and then prints out a
list of all the divisors of that number.

"""

num = int(input("Enter a number to divide: "))

range_list = list(range(1, num + 1))

divisor_list = []

for number in range_list:
    if num % number == 0:
        divisor_list.append(number)

print(divisor_list)
