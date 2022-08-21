import os 
from dotenv import load_dotenv 

__version__ = "0.0.0"

load_dotenv()

DISCORD_TOKEN = os.getenv('DISCORD_TOKEN')
DISCORD_GUILD = os.getenv('DISCORD_GUILD')
API_URL = os.getenv('API_URL')

