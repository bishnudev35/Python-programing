import requests  # pyright: ignore[reportMissingModuleSource]


r = requests.get('https://api.github.com/users/bishnudev35')
# print(r.text)

with open("Bishnu.txt",'w') as f:
    f.write(r.text)

