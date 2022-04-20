

plural = input("Enter a word: ")
if plural.endswith('s'):
    plural += 'es'
else:
    plural += 's'
print("The plural of", plural, "is", plural)
