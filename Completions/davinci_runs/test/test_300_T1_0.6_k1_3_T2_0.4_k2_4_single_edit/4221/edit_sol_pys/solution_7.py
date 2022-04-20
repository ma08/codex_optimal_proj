

plural = input("Enter a word: ")
if plural.endswith("s"):
    plural += "es"
else:
    plural += "s"
print(plural)
