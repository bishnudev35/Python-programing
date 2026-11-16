#Write a program that writes three lines of text to a file tasks.txt .
with open('tasks.txt','w') as f:
    string='''
Task1:lern Python
Task2:practice Python
Task3:build some thing new using it'''
    f.write(string)


#Open tasks.txt in append mode and add a new line 'Task Completed!'

with open('tasks.txt','a')as f:
    f.write("\nTask Completed!")

#Read the file and print all lines as list using readlines()

with open('tasks.txt','r')as f:
    content=f.readlines()
    print(content)