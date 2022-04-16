

name = input()

compact = ""

for i in range(len(name)):
    if i == 0 or name[i] != name[i - 1]:
        compact += name[i]

print(compact)
