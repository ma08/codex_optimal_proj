

plural = input("Enter your word: ")
if plural.endswith('s'):
    plural += 'es'
else:
    plural += 's'
print(plural)
