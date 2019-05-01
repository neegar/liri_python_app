import os, inquirer, dotenv, sys, requests, json
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv('API_KEY')

questions = [
  inquirer.List('choice',
                message="What do you want? ",
                choices=['movie', 'wikipedia', 'book', 'song', 'quit'],
            ),
]
answers = inquirer.prompt(questions)

if answers['choice'] == 'movie':
    movie_name = input("Enter the movie name: ")
    URL = f"http://omdbapi.com/?apikey={api_key}&t={movie_name}"
    result = requests.get(URL)
    movie = json.loads(result.content)
    print(movie['Title'])
    print(movie['Genre'])
    print(movie['Actors'])
    




