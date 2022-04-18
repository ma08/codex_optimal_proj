

name = input()

compacted = name[0] #initialize the first character

for i in range(1,len(name)):
    if name[i] != name[i-1]: #if the character is not the same as the previous one
        compacted += name[i]

print(compacted)
