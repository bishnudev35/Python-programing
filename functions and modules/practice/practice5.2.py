# install and import the requests module (if available) and use
# it to fetch date form "https://api.github.com" .

import requests


response=requests.get("https://api.github.com")

print(response.json())