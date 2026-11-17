import os
import requests
from dotenv import load_dotenv 

# 1. Load variables from your .env file
load_dotenv()

# 2. Retrieve the API key from the environment
API_KEY = os.getenv("API_KEY")
try:
    query=input('What type of news do you want today?\n')

    url = ('https://newsapi.org/v2/everything?'
           f'q={query}&'
           'from=2026-11-17&'
           'sortBy=popularity&'
           f'apiKey={API_KEY}')

    # print(url)
    r=requests.get(url)
    data=r.json()
    print(data)
except Exception as e:
    print("some error occour!",e)