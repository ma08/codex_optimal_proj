

name = input()

compacted = ""

for i in range(len(name)):
    if name[i] != name[i - 1] or i == 0:
        compacted += name[i]

print(compacted)
