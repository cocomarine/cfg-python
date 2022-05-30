# Project 1 extension:
# Use different stats for the Pokemon from the API
import random
import requests

def get_stats():
    ID = random.randint(1, 151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(ID)

    response = requests.get(url)
    pokemon = response.json()

    # different stats chosen
    # number of 'moves' to be compared, so len() used
    stats = {
        'name': pokemon['name'],
        'base_experience': pokemon['base_experience'],
        'order': pokemon['order'],
        'moves': len(pokemon['moves'])
    }

    return stats

def run():
    player = get_stats()
    print("Your Pokemon is chosen: {}".format(player['name']))
    opponent = get_stats()
    print("Opponent's Pokemon is chosen: {}".format(opponent['name']))

    stat_choice = input("\nWhich stat do you want to choose? (base_experience, order, moves) ").lower()

    print("Your Pokemon stats: {}".format(player[stat_choice]))
    print("Opponent's Pokemon stats: {}".format(opponent[stat_choice]))

    if player[stat_choice] > opponent[stat_choice]:
        print("You won!")
    elif player[stat_choice] < opponent[stat_choice]:
        print("You lost!")
    else:
        print("You drew!")

run()
