import requests
from settings import API_URL

page = 1

def get_people():      
    
    req = requests.get("https://swapi.dev/api/people/{}".format(page))
    content = req.json()              

    return content, page

