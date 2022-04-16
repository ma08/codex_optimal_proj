
name = input("Enter a string: ")

compact = ""

for i in range(len(name)):
    if name[i] != name[i - 1]:
        compact += name[i]

print(compact)
