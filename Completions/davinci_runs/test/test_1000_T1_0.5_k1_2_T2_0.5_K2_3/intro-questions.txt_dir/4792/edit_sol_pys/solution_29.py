

name = input("Enter a string: ")

i = 1

while i < len(name):
    if name[i] == name[i - 1]:
        name = name[:i] + name[i + 1:]
        i = i - 1
    else:
        i = i + 1

print(name)
