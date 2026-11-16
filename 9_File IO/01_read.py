try:
    f=open("demo.txt",'rt')
    content=f.read()
    print(content)
    f.close()
except FileNotFoundError :
    print("file not found.")