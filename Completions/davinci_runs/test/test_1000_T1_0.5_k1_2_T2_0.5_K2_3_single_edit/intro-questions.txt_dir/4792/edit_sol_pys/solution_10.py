
name = input()

for i in range(0,len(name)):
    if name[i] == name[i+1]:
        name = name[:i] + name[i+2:]
        i -= 2

print(name)
