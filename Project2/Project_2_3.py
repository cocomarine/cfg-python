# Project 2: Search
# Extention 3: Ask the user additional questions to decide which recipe they should choose

import requests
from pprint import pprint

def recipe_search(ingredient):
    app_id = 'XXXX'
    app_key = 'XXXX'

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    response = requests.get(url)
    data = response.json()
    return data

def run():
    ingredient = input("Which ingredient you want to search for? ")
    results = recipe_search(ingredient)['hits']

    # additional input for low-carb recipes
    additional = input("Do you want to choose low-carb recipes? (y/n) ")

    for result in results:
        recipe = result['recipe']

        # if user input yes ('y'), extract and print the recipes with 'Low-Carb' label
        if additional == 'y'.lower():
            for dl in recipe['dietLabels']:
                if dl == 'Low-Carb':
                    print("\n" + recipe['label'])
                    print(recipe['url'])
        # if user input no ('n'), print out all the recipes
        else:
            print("\n" + recipe['label'])
            print(recipe['url'])

run()
