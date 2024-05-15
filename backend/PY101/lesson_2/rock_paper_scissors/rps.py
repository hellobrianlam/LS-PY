import random

VALID_CHOICES = ["Rock", "Paper", "Scissors", "Lizard", "Spock"]

# SHORTENED_CHOICES = ['Rk', 'Pr', 'Sr', 'Ld', 'Sk']

WINNING_COMBOS = {
    'Rock':     ['Scissors', 'Lizard'],
    'Paper':    ['Rock',     'Spock'],
    'Scissors': ['Paper',    'Lizard'],
    'Lizard':   ['Paper',    'Spock'],
    'Spock':    ['Rock',     'Scissors'],
}

game_scoreboard = {
        'User':     0,
        'Computer': 0,
        'Draw': 0
}

def update_score(player):
    if player in game_scoreboard:
        game_scoreboard[player] += 1

def prompt(message):
    '''
    prepend the marker to the front of each output string we pass to print
    '''
    print(f"==> {message}")

def player_wins(player_choice, computer_choice):
    return computer_choice in WINNING_COMBOS[player_choice]

# def computer_wins(player_choice, computer_choice):
#     return player_choice in WINNING_COMBOS[computer_choice]

def display_winner(player, computer):
    prompt(f"You chose {player}, computer chose {computer}")

    if player_wins(player, computer):
        update_score('User')
        prompt("You win!")
        prompt(game_scoreboard)

    elif player == computer:
        update_score('Draw')
        prompt("It's a tie!")
        prompt(game_scoreboard)
    else:
        update_score('Computer')
        prompt("Computer wins!")
        prompt(game_scoreboard)

while max(game_scoreboard.values()) < 3:
    prompt(f'Choose one: {", ".join(VALID_CHOICES)}')
    choice = input().capitalize()

    while choice not in VALID_CHOICES:
        prompt("That's not a valid choice")
        choice = input().capitalize()

    computer_choice = random.choice(VALID_CHOICES)

    display_winner(choice, computer_choice)

prompt(f"The Grand Winner is {max(game_scoreboard, key=lambda k: game_scoreboard[k])}")

prompt("Do you want to play again (y/n)?")
answer = input().lower()
while answer == '' or (answer[0] != 'n' and answer[0] != 'y'):
    prompt('Please enter "y" or "n".')
    answer = input().lower()

    if answer[0] != "y":
        break