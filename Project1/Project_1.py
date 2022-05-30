import random
import requests


def get_stats():
    ID = random.randint(1, 151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(ID)

    response = requests.get(url)
    pokemon = response.json()

    stats = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

    return stats


def run():
    player = get_stats()
    print("Your Pokemon is chosen: {}".format(player['name']))
    opponent = get_stats()
    print("Opponent's Pokemon is chosen: {}".format(opponent['name']))

    stat_choice = input("\nWhich stat do you want to choose? (id, weight, height) ").lower()

    print("Your Pokemon stats: {}".format(player[stat_choice]))
    print("Opponent's Pokemon stats: {}".format(opponent[stat_choice]))

    if player[stat_choice] > opponent[stat_choice]:
        print("You won!")
    elif player[stat_choice] < opponent[stat_choice]:
        print("You lost!")
    else:
        print("You drew!")

run()
