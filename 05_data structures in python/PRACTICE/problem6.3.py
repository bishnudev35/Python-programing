# Write a program that merges two dictionaries into one.
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Method 1: Merge operator (Python 3.9+)
merged_dict = dict1 | dict2

# Method 2: Unpacking operator (works in all Python 3 versions)
# merged_dict = {**dict1, **dict2}

print(merged_dict)

# or
dict1 = {"a": 1, "b": 2}
dict2 = {"c": 3, "d": 4}

# Make a copy so dict1 stays unchanged
merged_dict = dict1.copy()

# Merge dict2 into the copy
merged_dict.update(dict2)

print(merged_dict)
