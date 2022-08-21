import requests
from settings import API_URL

def get_people(informed_page):      
    
    page = informed_page
    req = requests.get("https://swapi.dev/api/people/{}".format(page))
    content = req.json()              

    return content, page

