

name = str(input())

compact = ""

for i in range(len(name)):
    if i == 0:
    elif name[i] != name[i - 1]:
        compact += name[i]

        compact += name[i]

print(compact)
