

name = input()  # input string

compacted = name[0]  # first character

for i in range(1, len(name)):
    if name[i] != name[i - 1]:
        compacted += name[i]

print(compacted)
