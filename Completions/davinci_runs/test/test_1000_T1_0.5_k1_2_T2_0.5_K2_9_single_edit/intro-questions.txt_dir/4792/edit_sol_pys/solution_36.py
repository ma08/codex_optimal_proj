def remove_duplicates(name):
    for i in range(1, len(name)):
        if name[i] == name[i - 1]:
            name = name[:i] + name[i + 1:]
            i -= 1
    return name

name = input()
name = remove_duplicates(name)

print(name)
