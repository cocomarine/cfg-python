# Project 1 extension: Record high scores for players and store them in a file
import random
import requests
import csv


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

    # for each run, winner and winning score stored in data dictionary
    who = ""
    score = 0
    if player[stat_choice] > opponent[stat_choice]:
        print("You won!")
        who = "player"
        score = player[stat_choice]
    elif player[stat_choice] < opponent[stat_choice]:
        print("You lost!")
        who = "opponent"
        score = opponent[stat_choice]
    else:
        print("You drew!")
        who = "both"
        score = player[stat_choice]

    data = [
        { 'who' : who, 'chosen_stat' : stat_choice, 'winning_score' : score
        }]
    return data


def write_file():
    rounds = int(input("How many rounds? "))

    field_names = ['who', 'chosen_stat', 'winning_score']

    # results to be recorded in a csv file
    with open('poke_high_scores.csv', 'w+') as csv_file:
        spreadsheet = csv.DictWriter(csv_file, fieldnames=field_names)

        spreadsheet.writeheader()

        # returned data dictionary after each round is written as row in the file
        for i in range(rounds):
            print("Round {}\n".format(i + 1))
            data = run()
            print("\n")
            spreadsheet.writerows(data)


write_file()
