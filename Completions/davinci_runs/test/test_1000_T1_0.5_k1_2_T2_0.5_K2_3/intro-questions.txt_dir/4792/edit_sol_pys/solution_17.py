

name = input("Enter the string: ")
name = name.split(" ")
for i in range(len(name)):
    name[i] = name[i].capitalize()
print(*name)



