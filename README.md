# Recipe Directory Database

## Introduction
- This is a challenge in Makers Module 3 - Databases
- I set up this project using a starter project from Makers, as per the challenge instructions below.
- This project includes a `recipes` database, containing a `recipes` table.
- The main program `app.py` prints a list of all the recipes in the database to the terminal.
- `recipes_schema_recipe.md` documents my design of the `recipes` table

## Objectives
- [x] Learn to test-drive a Repository class method to SELECT a single record from the database.
- [x] Design and create a table for the following user stories:  
  - [x] As a food lover,  
        So I can stay organised and decide what to cook,  
        I'd like to keep a list of all my recipes with their names.
  - [x] As a food lover,  
        So I can stay organised and decide what to cook,  
        I'd like to keep the average cooking time (in minutes) for each recipe.
  - [x] As a food lover,  
        So I can stay organised and decide what to cook,  
        I'd like to give a rating to each of the recipes (from 1 to 5).
- [x] Create a seeds/recipes.sql.
- [x] Test-drive a Recipe class that has attributes for each column in your table.
- [x] Test-drive a RecipeRepository class that has all and find methods.
- [x] Write a small program in app.py using the class RecipeRepository to print out the list of recipes to the terminal.

## Setup
This project uses `python`, `pyenv` and `pipenv`. Here's how to install it:

```shell
# Install pyenv, a tool to manage different versions of Python.
# This will ensure you have the latest Python, which has more readable error messages.
; brew install pyenv
# You may be given some extra instructions at the end of the command.
# If you are, follow them. If not, keep going.

# Now install the latest Python.
; pyenv install 3.11

# Install pipenv
; python3 -m ensurepip --upgrade
; pip3 install --user pipenv
; echo 'export PATH="$PATH:$(python3 -m site --user-base)/bin" # Add Pipenv to PATH' >> ~/.zshrc
; source ~/.zshrc
; pipenv --version # Check pipenv is installed
pipenv, version ...

# Clone the repository to your local machine
; git clone https://github.com/NatalieJClark/recipe-directory-database.git YOUR_PROJECT_NAME

# Enter the directory
; cd YOUR_PROJECT_NAME

# Install dependencies and set up the virtual environment
; pipenv install

# Activate the virtual environment
; pipenv shell
# NB: you may need to change interpreter path, to import pytest and psycopg
# This will give you the path to use
; pipenv --venv

# Create the database
; createdb YOUR_PROJECT_NAME

# Open lib/database_connection.py and change the database name to YOUR_PROJECT_NAME
; open lib/database_connection.py

# Run the tests
; pytest

# Run the app
; python app.py

# To exit the pipenv shell
; exit # or Ctrl-D
