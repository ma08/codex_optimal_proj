

name = input()  # input name

compact = ""

for i in range(1, len(name)):
    if name[i] != name[i - 1]:
        compact += name[i]

print(compact)
