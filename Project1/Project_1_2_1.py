# Project 1 extension: get multiple random Pokemons and
# let the player decide which one that they want to use
import random
import requests


def get_stats(url):
    response = requests.get(url)
    pokemon = response.json()

    stats = {
        'name': pokemon['name'],
        'id': pokemon['id'],
        'height': pokemon['height'],
        'weight': pokemon['weight']
    }

    return stats


# generating random pokemons and returning their stats
def random_poke():
    ID = random.randint(1, 151)

    url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(ID)

    return(get_stats(url))


# for returning stats of a chosen pokemon
def chosen_stats(name):
        url = 'https://pokeapi.co/api/v2/pokemon/{}'.format(name)

        return (get_stats(url))


def run():
    x = int(input("How many Pokemons? "))
    # for-loop for generating x number of pokemons
    for i in range(x):
        each_poke = random_poke()
        print(each_poke['name'])

    player_chosen = input("\nWhich Pokemon do you want to choose? ")
    player = chosen_stats(player_chosen)
    print("Your Pokemon is chosen: {}".format(player['name']))

    opponent = random_poke()
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
