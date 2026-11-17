import re

text='The quick brown fox jumps over the lazy dog.'

'''#search for a pattern
match=re.search('brown',text)
print(match)
if match:
    print("Match found!")
    print('Start index:',match.start())
    print('End index:',match.end())'''

#find all occurrences of a pattern
matches=re.findall('the',text,re.IGNORECASE)#case insensitive serch
print('Matches:',matches)