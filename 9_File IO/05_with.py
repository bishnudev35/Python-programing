# f=open("demo.txt",'rt')
# content=f.read()
# print(content)
# f.close()

with open("demo.txt",'r') as f:#context manager
    content=f.read()
    print(content)
    #no need to write f.close() because file is already closed by default
    #whe using with syntax