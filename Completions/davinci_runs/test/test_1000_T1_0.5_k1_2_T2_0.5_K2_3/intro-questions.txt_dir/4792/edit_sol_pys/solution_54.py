

name = input("Enter your name: ")

compacted = name[0].upper()

for i in range(1,len(name)):
    if name[i] != name[i-1]:
        compacted += name[i].upper()

print("Your compacted name is: ", compacted)
