# Project 1 required tasks
import random
import requests


def get_stats():
    # a random integer between 1-151 generated as a pokemon ID
    ID = random.randint(1, 151)

    # pokeapi address correponding to the ID
    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(ID)

    # json file saved in pokemon variable
    response = requests.get(url)
    pokemon = response.json()

    # pokemon stats pulled out from jason and saved in and returned as stats dictionary an
    stats = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

    return stats


def run():
    # getting stats for player and opponent
    player = get_stats()
    print("Your Pokemon is chosen: {}".format(player['name']))
    opponent = get_stats()
    print("Opponent's Pokemon is chosen: {}".format(opponent['name']))

    # stat chosen by player stored in stat_choice
    stat_choice = input("\nWhich stat do you want to choose? (id, weight, height) ").lower()

    # showing chosen stat's values for player and opponent
    print("Your Pokemon stats: {}".format(player[stat_choice]))
    print("Opponent's Pokemon stats: {}".format(opponent[stat_choice]))

    # Deciding who's stat wins
    if player[stat_choice] > opponent[stat_choice]:
        print("You won!")
    elif player[stat_choice] < opponent[stat_choice]:
        print("You lost!")
    else:
        print("You drew!")

run()
