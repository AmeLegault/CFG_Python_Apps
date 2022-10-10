import random
import requests
import sys
import os
import csv
import pandas as pd
field_names = ['Name', 'Score']

global player_score
global computer_score
player_score = 0
computer_score = 0


player_name = input('Hello! What is your name? ')
print('Welcome {} to the Best Top Trump Game for Geeks!\n'.format(player_name))
menu = input('What would you like to do? Play or Scores? ').title()

if menu == 'Play':
    game_choice = input("Which game would you like to play? Pokemon or Smash Brothers ").title()
elif menu == 'Scores':
    with open("score.csv", "r") as csv_file:
        scores = pd.read_csv("/Users/Aamelie/PycharmProjects/PythonClassAndApps/score.csv", index_col="Name")
        sorted_scores = scores.sort_values(["Score"], axis=0, ascending=[False], inplace=False)
        high_scores = sorted_scores.head(5)
        print(high_scores)
    game_choice = input("Which game would you like to play? Pokemon or Smash Brothers ").title()
else:
    print("This is not one of the choices! Try again.")
    os.execv(sys.executable, ['python'] + sys.argv)


def random_pokemon():
    pokemon_number = random.randint(1, 151)
    url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number)
    response = requests.get(url)
    pokemon = response.json()

    return {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight'],
        'items': len(pokemon['held_items'])
    }


def play_pokemon():
    global player_score
    global computer_score
    player1_choice1 = random_pokemon()
    player1_choice2 = random_pokemon()
    print("\nIn this Pokemon game you will choose between two different Pokemons.\n"
          "You then need to choose which stat you would like to use to go up against the computer.\n"
          "If your stat is higher, you win. If it is lower, you lose.\n")
    choice = input('Which Pokemon would you like to play with? {} or {}? '.format(player1_choice1['name'],
                                                                                  player1_choice2['name']))
    if choice == player1_choice1['name']:
        player1_pokemon = player1_choice1
    elif choice == player1_choice2['name']:
        player1_pokemon = player1_choice2
    else:
        print("This was not one of the choices. Choose again.")
        play_pokemon()
    print('You chose: {}'.format(player1_pokemon['name'].capitalize()))
    stat = input('Which stat would you like to use? (id, height, weight, items) ')
    player2_pokemon = random_pokemon()
    player1_stat = player1_pokemon[stat]
    player2_stat = player2_pokemon[stat]
    print('Your Pokemon is {}. Its {} is {}.\n'
          'It goes up against {} who has a {} of {}.\n'.format(player1_pokemon['name'].capitalize(), stat, player1_stat,
                                                            player2_pokemon['name'].capitalize(), stat, player2_stat))
    if player1_stat > player2_stat:
        print('You are the Pokemon Master!')
        player_score += 1
        print('Your score: {}. Player 2 score: {}.\n'.format(player_score, computer_score))
    elif player1_stat < player2_stat:
        print('Go back to training.')
        computer_score += 1
        print('Your score: {}. Player 2 score: {}.\n'.format(player_score, computer_score))
    else:
        print('Tie! Try again')
        print('Your score: {}. Player 2 score: {}.\n'.format(player_score, computer_score))
    play_again = input('Would you like to play again? yes or no ')
    if play_again == 'yes' or play_again == ' yes':
        play_pokemon()
    else:
        print('Hope you enjoyed the game!')
        with open('score.csv', 'a') as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
            spreadsheet.writerows([{'Name': player_name, 'Score': player_score}])


def random_smash():
    smash_number = random.randint(1, 26)
    url = 'http://smashlounge.com/api/chars/{}'.format(str(smash_number))
    response_smash = requests.get(url)
    smash = response_smash.json()

    return {
        'name': smash["name"],
        'id': smash["id"],
        'tierdata': smash['tierdata'],
    }


def play_smash():
    global player_score
    global computer_score
    player1_choice1 = random_smash()
    player1_choice2 = random_smash()
    print("\nIn this game you will choose between two different Smash Brothers characters.\n"
          "You then need to choose which stat you would like to use to go up against the computer.\n"
          "In this case, the tierdata references to the rank of the character.\n"
          "This means that if your stat is a lower number, you win. If it is higher, you lose.\n")
    choice = input('Which character would you like to play with? {} or {}? '.format(player1_choice1['name'],
                                                                                    player1_choice2['name'])).title()
    if choice == player1_choice1['name']:
        player1_smash = player1_choice1
    elif choice == player1_choice2['name']:
        player1_smash = player1_choice2
    else:
        print("This was not one of the choices. Choose again.")
        play_smash()
    print('You chose: {}'.format(player1_smash['name']))
    stat = input('Which stat would you like to use? (id or tierdata) ')
    player2_smash = random_smash()
    player1_stat = player1_smash[stat]
    player2_stat = player2_smash[stat]
    print('Your character is {}. Its {} is {}.\n'
          'It goes up against {} who has a {} of {}.\n'.format(player1_smash['name'], stat, player1_stat,
                                                               player2_smash['name'], stat, player2_stat))
    if player1_stat < player2_stat:
        print('You smashed it!')
        player_score += 1
        print('Your score: {}. Player 2 score: {}.\n'.format(player_score, computer_score))
    elif player1_stat > player2_stat:
        print('Go back to training.')
        computer_score += 1
        print('Your score: {}. Player 2 score: {}.\n'.format(player_score, computer_score))
    else:
        print('Tie! Try again')
        print('Your score: {}. Player 2 score: {}.\n'.format(player_score, computer_score))
    play_again = input('Would you like to play again? yes or no ')
    if play_again == 'yes' or play_again == ' yes':
        play_smash()
    else:
        print('Hope you enjoyed the game!')
        with open('score.csv', 'a') as csv_file:
            spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)
            spreadsheet.writerows([{'Name': player_name, 'Score': player_score}])


if game_choice == "Pokemon":
    play_pokemon()
elif game_choice == "Smash Brothers":
    play_smash()
else:
    print("This is not one of the choices! Try again.")
    os.execv(sys.executable, ['python'] + sys.argv)
