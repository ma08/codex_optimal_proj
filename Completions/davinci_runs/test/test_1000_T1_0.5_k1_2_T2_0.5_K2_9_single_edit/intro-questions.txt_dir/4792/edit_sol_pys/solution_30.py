

name = input()

compacted = [name[0]]

for i in range(1,len(name)):
    if name[i] != name[i-1]:
        compacted.append(name[i])

print("".join(compacted))
