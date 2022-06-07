# Project 2 required tasks

import requests

def recipe_search(ingredient):
    app_id = '0d951222'
    app_key = '14d6cfc30995f17bde17b1441195a139'

    # edamam api address of an ingredient
    url = 'https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key)

    # json file saved in data variable
    response = requests.get(url)
    data = response.json()

    return data

def run():
    ingredient = input("Which ingredient you want to search for? ")
    # values corresponding to hits key saved in results
    results = recipe_search(ingredient)['hits']

    # for-loop going through items in results
    for result in results:
        # recipe key values saved in recipe
        recipe = result['recipe']
        # recipe title ('label') printed followed by address ('url')
        print("\n" + recipe['label'])
        print(recipe['url'])

run()

