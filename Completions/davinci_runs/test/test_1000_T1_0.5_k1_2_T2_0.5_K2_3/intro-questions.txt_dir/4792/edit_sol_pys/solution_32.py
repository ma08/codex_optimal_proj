# this is my name,
name = input()

print(name[0], end="")
for i in range(1, len(name)):
    if name[i] != name[i - 1]:
        print(name[i], end="")
