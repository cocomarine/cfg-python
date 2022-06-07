### Project Brief: Search
In addition to the final project I have chosen (Project 1), I also worked on the other two projects in my own time. 
Again, I worked on the required tasks first and then modified it to incorporate some of the extensions and variations. 

### Instruction
In this project you'll create a program to search for recipes based on an ingredient. The standard
project uses the Edamam Recipe API, but can be changed to use a different API after completing
the required tasks.
You will not need any additional knowledge beyond what is covered in this course to complete this
project.

### Setup
To use the Edamam API you will need to register for an account. In your Edamam account
dashboard you can find an Application ID and Application Key, which you will need to make
requests to the API.
To make a request to the Edamam API use the following URL:
https://api.edamam.com/search?q={INGREDIENT}&app_id={YOUR_APP_KEY}&app_key={YOUR_
APP_KEY}
For example, if the App ID and App Key for me account were “ch37j44” and “a58hia” I wanted to
search for “cheese”, the url would look like this:
https://api.edamam.com/search?q=cheese&app_id=ch37j44&app_key=a58hia

### Required Tasks
These are the required tasks for this project. You should aim to complete these tasks before
adding your own ideas to the project.
1. Read the Edamam API documentation ★
https://developer.edamam.com/edamam-docs-recipe-api
2. Ask the user to enter an ingredient that they want to search for
3. Create a function that makes a request to the Edamam API with the required ingredient as
part of the search query (also included your Application ID and Application Key
4. Get the returned recipes from the API response
5. Display the recipes for each search result

#### Ideas for Extending the Project
Here are a few ideas for extending the project beyond the required tasks. These ideas are just
suggestions, feel free to come up with your own ideas and extend the program however you want.
● Save the results to a file
● Order the results by weight or another piece of data
● Ask the user additional questions to decide which recipe they should choose
● Cross-reference the ingredient against the Edamam nutrition analysis API
● Use a different searchable API (suggestions in useful resources)
