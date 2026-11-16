def func(*args,**kwargs):
    print(args)
    print(kwargs)

func(1,23,4,5,jack=23,jill=33,marie=66)
# output
# (1, 23, 4, 5)
# {'jack': 23, 'jill': 33, 'marie': 66}