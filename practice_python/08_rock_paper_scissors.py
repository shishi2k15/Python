"""
Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays
(using input), compare them, print out a message of congratulations to the
winner, and ask if the players want to start a new game)

Remember the rules:

Rock beats scissors
Scissors beats paper
Paper beats rock
"""
choice_dict = {'rock': 'scissors',
               'scissors': 'paper',
               'paper': 'rock'}


def game(choice_1, choice_2):
    if choice_1 == choice_2:
        return 'Draw'
    elif choice_dict[choice_1] == choice_2:
        return 'Player 1 wins !'
    else:
        return 'Player 2 wins !'

while True:
    player_1 = str(raw_input('Player 1: '))
    player_2 = str(raw_input('Player 2: '))

    print(game(player_1, player_2))

    play_again = str(raw_input('Play again ? y/n: \n'))
    if play_again.lower() == 'n':
        break
