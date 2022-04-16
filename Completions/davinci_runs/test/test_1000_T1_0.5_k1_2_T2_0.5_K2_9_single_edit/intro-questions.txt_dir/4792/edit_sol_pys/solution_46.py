
name = input()

compact = ""

for i in range(len(name)):
    if name[i] != name[i - 1] and name[i] != ' ':
        compact += name[i]

print(compact)
