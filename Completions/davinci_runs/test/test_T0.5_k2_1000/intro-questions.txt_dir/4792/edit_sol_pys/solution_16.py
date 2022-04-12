

name = input("Enter your name: ").lower()

compact = ""

for i in range(len(name) - 1):
    if name[i] != name[i + 1]:
        compact += name[i + 1]

print(compact)
