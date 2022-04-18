

#gets input
name, parent = input().split()

#checks if name ends in "a"
if name[-1] == "a":
    print(name + "x" + parent)
#checks if name ends in "ix"
elif name[-2:] == "ix":
    print(name + parent)
#checks if name ends in "o"
elif name[-1] == "o":
    print(name[:-1] + "ix" + parent)
#otherwise, adds "ix"
else:
    print(name + "ix" + parent)
