

name = input("Enter your name: ")

i = 0

while i < len(name) - 1:
    if name[i] == name[i + 1]:
        name = name[:i + 1] + name[i + 2:]
    else:
        i += 1

print(name)
