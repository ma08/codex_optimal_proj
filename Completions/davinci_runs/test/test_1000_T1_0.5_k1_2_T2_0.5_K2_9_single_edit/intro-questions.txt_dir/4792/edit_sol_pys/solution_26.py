

name = input("Enter your name: ")
new_name = ""

for i in range(len(name)):
    if i == 0:
        new_name += name[0]
    elif name[i] != name[i-1]:
        new_name += name[i]

print(new_name)
