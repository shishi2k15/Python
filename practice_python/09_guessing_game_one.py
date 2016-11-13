'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low,
 too high, or exactly right. (Hint: remember to use the user input lessons
 from the very first exercise)
'''
import random

rand_num = random.randint(1, 9)
guess = 0
tries = 0

print('Guess the number')

while int(guess) != rand_num and str(guess) != 'exit':
    guess = raw_input('>> ')

    if str(guess) == 'exit':
        break

    guess = int(guess)
    tries += 1

    if guess < rand_num:
        print('Try higher...')

    if guess > rand_num:
        print('Try lower...')

    if guess == rand_num:
        print('[+] You win, the number is {} with {} tries'.format(rand_num,
                                                                   tries))
        break
