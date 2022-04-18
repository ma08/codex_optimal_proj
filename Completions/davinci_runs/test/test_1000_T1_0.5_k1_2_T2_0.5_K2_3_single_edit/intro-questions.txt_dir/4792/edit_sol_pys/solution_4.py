

name = input()
for i in range(1,len(name)):
    if name[i] == name[i-1] and name[i] != ' ':
        name = name[:i] + name[i+1:]
        i -= 1

print(name)
