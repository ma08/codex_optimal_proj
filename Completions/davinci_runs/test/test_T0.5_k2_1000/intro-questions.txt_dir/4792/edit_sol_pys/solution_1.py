

name = input("Enter your name: ")

compacted = ""

for i in range(len(name)):
    if name[i] != name[i - 1]:
        compacted += name[i]

print(compacted)
