

name = input("Enter your name: ")

compacted = ""

for i in range(1,len(name)):
    if name[i] != name[i-1]:
        compacted += name[i]

print("Your compacted name is: ", compacted)
