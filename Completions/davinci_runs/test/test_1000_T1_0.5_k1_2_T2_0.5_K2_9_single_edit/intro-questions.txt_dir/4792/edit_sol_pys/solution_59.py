

name = input()
compact = name[0]

for i in range(len(name)):
    if name[i] != compact[-1]:
        compact += name[i]

print(compact)
