
# 1.Create a text file notes.txt usnig Python and write "Learning Python is fun!" into it


f=open("notes.txt",'w')

string='Learning Python is fun!'

f.write(string)
f.close()

# 2.Open notes.text, read it content and print it to the console.
f=open('notes.txt','r')
content=f.read()
print(content)
f.close()

