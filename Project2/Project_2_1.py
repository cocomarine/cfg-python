# Project 2: Search
# Extention 1: Save the results to a file

import requests

def recipe_search(ingredient):
    app_id = 'XXXX'
    app_key = 'XXXX'

    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    response = requests.get(url)
    data = response.json()
    return data

def run():
    ingredient = input("Which ingredient you want to search for? ")
    # values corresponding to hits key saved in results
    results = recipe_search(ingredient)['hits']

    # recipes to be recorded in a text file
    with open('recipes.txt', 'w') as text_file:

        # for-loop going through items in results
        for result in results:
            # recipe key values saved in recipe
            recipe = result['recipe']
            text_file.write(recipe['label'] + "\n")
            text_file.write(recipe['url'] + "\n\n")

run()


