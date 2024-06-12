import requests

# RAWG API
API_KEY='28cf94e72b3e4b58ae035677b43bcfd7'


# takes query parameter as a string
# makes GET request to API endpoint using requests.get() and passing params as query string
# returns results as a json which is a games object retrieved from the search query
def search_games(query):
    url=f'https://api.rawg.io/api/games'
    params = {
        'key':API_KEY,
        'search':query,
        'page_size':10
    }
    response=requests.get(url,params=params)
    return response.json()['results']


# takes game_id as param
# sets param as just key and defines url to send req to get a specific game based on its id
# returns game object retrieved from the API
def get_game_details(game_id):
    url=f'https://api.rawg.io/api/games/{game_id}'
    params = {'key': API_KEY}
    response = requests.get(url,params=params)
    return response.json()