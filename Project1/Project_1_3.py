# Project 1 extension: Play multiple rounds and record the outcome of
# each round. The player with most number of rounds won, wins the game
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

    stat_choice = input("\nWhich stat do you want to choose? ").lower()

    print("Your Pokemon stats: {}".format(player[stat_choice]))
    print("Opponent's Pokemon stats: {}".format(opponent[stat_choice]))

    # returning winnings as 1, -1 or 0 so that their sum after several rounds
    # can be used to see who won the most
    if player[stat_choice] > opponent[stat_choice]:
        print("You won!")
        return 1
    elif player[stat_choice] < opponent[stat_choice]:
        print("You lost!")
        return -1
    else:
        print("You drew!")
        return 0


def multi_rounds():
    rounds = int(input("How many rounds? "))
    total_win = 0

    # for each round, 1, -1 or 0 added to total_win
    for i in range(rounds):
        print("Round {}".format(i+1))
        x = run()
        total_win += x
        print("\n")

    # printing out who won based on total_win
    if total_win > 0:
        print("After {} rounds, you won!".format(rounds))
    elif total_win < 0:
        print("After {} rounds, you lost!".format(rounds))
    else:
        print("After {} rounds, you drew!".format(rounds))


multi_rounds()