def marks(**kwargs):
    #kwargs is a dictionary with all the key value pairs which were passed to marks
    for item in kwargs.keys():
        print(f"The marks of {item} is {kwargs[item]}")

marks(subham=23,vikrant=34,jack=33,marie=90)
