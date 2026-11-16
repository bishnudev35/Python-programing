# Write to a file callded John Doe.txt
# it should contain data about John Doe

f=open("John Doe.txt",'w')

string='''
John Doe is a nice guy. He lives in Nyc and he works wit Python.
His favorite package is Pandas.'''

f.write(string)
f.close()