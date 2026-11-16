#Append to an exisiting file callded John Doe.txt
# it should contain data about John Doe
f=open("John Doe.txt",'a')

string='''
John Doe initially lived in Phoenix, Arizona. He is a very nice guy'''

f.write(string)
f.close()