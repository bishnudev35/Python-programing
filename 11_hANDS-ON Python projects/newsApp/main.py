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
           'sortBy=popularity&'
           f'apiKey={API_KEY}')

    # print(url)
    r=requests.get(url)
    data=r.json()
   # print(data)
    articles=data['articles']
    i=1
    for article in articles:
        print(i,article['title'],article['url'])
        i+=1
        print('\n**********************************************\n')

except Exception as e:
    print("some error occour!",e)