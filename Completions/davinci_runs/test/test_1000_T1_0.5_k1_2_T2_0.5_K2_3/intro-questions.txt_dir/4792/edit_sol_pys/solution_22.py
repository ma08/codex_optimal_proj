

name = input()

compactedName = name[0]

for i in range(1,len(name)):
    if name[i] != name[i - 1]:
        compactedName += name[i]

print(compactedName)
