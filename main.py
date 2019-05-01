import os, inquirer, dotenv, sys, requests, json, spotipy
from dotenv import load_dotenv

from spotipy.oauth2 import SpotifyClientCredentials
import pprint

import re
sys.path.append(os.path.realpath('.'))
from pprint import pprint

load_dotenv()

api_key = os.getenv('API_KEY')
 
client_id = os.getenv('client_id')
client_secret = os.getenv('client_secret')

while True:
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

    if answers['choice'] == 'song':
        
        singers_name = input("type singer's name: ")
        client_credentials_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
        sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
        result = sp.search(singers_name)
        print(dir(result['tracks']['items'][0].items))

    #tracks, items, album, name
    if answers['choice'] == 'quit':
        print("okay, i will go(")
        break

    

    questions = [
    inquirer.Confirm('continue',
                  message="Should I continue?"),
   
    ]

    answer = inquirer.prompt(questions)

    if answer['continue'] == False:
        print("See you soon")
        break


