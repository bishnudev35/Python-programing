#storng formatting

template='Dear {}, You are asweome. Take this ${} bag'

a='john'
a1=10000
b='Jack'
b1=1000
c='Marie'
c1=200

s1=template.format(a,a1)
print(s1)
s2=template.format(b,b1)
s3=template.format(c,c1)
print(s2)
print(s3)

# also we can use
print(f"{a} you are awesome and take this {a1}$ bag")