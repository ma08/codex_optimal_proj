

name = input("Enter your name: ")

compact = ""

for i in range(len(name)):
    if i == 0:
        compact += name[i]
    elif name[i] != name[i - 1]:
        compact += name[i]

print(compact)
