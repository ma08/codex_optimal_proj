

name = input("Enter the string: ")
name = name.split(" ") # split the string
for i in range(len(name)):
    name[i] = name[i].capitalize() # capitalize the first letter
    print(name[i], end = " ") # print the output



