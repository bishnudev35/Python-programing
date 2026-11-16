marks={"Harry":23,"Jack":23,"Bishnu":33}

print(marks,type(marks))

print(marks["Bishnu"])
marks["Harry"]=100
print(marks)

print(marks.keys())
print(marks.values())
marks.pop("Jack")
print(marks)
marks.clear()
print(marks)