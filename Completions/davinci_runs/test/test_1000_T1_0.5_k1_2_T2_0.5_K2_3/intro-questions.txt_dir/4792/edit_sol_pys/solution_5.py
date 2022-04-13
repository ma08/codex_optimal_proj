

name = input("Enter a name: ")

compacted_name = name[0]

for i in range(1,len(name)):
    if name[i] != name[i-1]:
        compacted_name += name[i]

print(compactedName)
