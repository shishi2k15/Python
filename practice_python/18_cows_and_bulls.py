from random import randint
import random

num = '0123456789'
code = ''.join(random.sample(num, 4))
attempt = 10


def compare_numbers(guess, code):
    """Compares the two numbers and counts the cows and bulls
    """
    cow_bulls = [0, 0]  # [0] is cows, [1] is bulls
    remaining_x = []
    remaining_y = []
    for x, y in zip(guess, code):
        if x == y:
            cow_bulls[1] += 1
        else:
            remaining_x.append(x)
            remaining_y.append(y)
    for x in remaining_x:
        if x in remaining_y:
            cow_bulls[0] += 1
            remaining_y.remove(x)

    return cow_bulls


def main():
    playing = True
    random_number = str(randint(1000, 2000))
    print(random_number)
    guesses = 0

    print("Let's play a game of Cowbull!")  # explanation
    print("I will generate a number, and you have to guess the numbers one\
          digit at a time.")
    print("For every number in the wrong place, you get a cow. For every one\
          in the right place, you get a bull.")
    print("The game ends when you get 4 bulls!")
    print("Type exit at any prompt to exit.")

    while playing:
        user_guess = input('Give me a wild guess: ')
        if user_guess == 'exit':
            break

        cow_bull_count = compare_numbers(user_guess, random_number)
        guesses += 1

        print("You have " + str(cow_bull_count[0]) + " cows, and " +
              str(cow_bull_count[1]) + " bulls.")

        if cow_bull_count[1] == 4:
            playing = False
            print('You win the game after ' + str(guesses) + '!\
                  The number was ' + str(random_number))
            break
        else:
            print('Try again.\n')

if __name__ == '__main__':
    main()
