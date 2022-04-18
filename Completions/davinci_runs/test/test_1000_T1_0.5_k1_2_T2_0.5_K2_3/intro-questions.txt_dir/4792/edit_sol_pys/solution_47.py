

name = input().strip()[::-1]

i = 1

while i < len(name) - 1:
    if name[i] == name[i - 1]:
        name = name[:i] + name[i + 1:] + name[i]
        i -= 1
    else:
        i += 1

print(name)
