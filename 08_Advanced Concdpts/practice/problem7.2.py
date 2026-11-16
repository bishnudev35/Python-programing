# Use the walrus operator in a list comprehension to store lengths of words
# from ["python", "rocks", "ai"] in a list while filtering out words shorter
#  than 4 characters.
words = ["python", "rocks", "ai"]

# Compute length once, filter words >= 4 characters, and store the length
lengths = [length for word in words if (length := len(word)) >= 4]

print(lengths)  # Output: [6, 5]
