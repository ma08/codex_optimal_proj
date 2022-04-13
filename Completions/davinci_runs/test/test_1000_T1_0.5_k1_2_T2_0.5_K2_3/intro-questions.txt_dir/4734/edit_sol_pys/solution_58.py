

#gets input
name, parent = input().split()

#checks if name ends in "a"
if name[-1] == "a":
    print(name + "x" + parent + "x")
#checks if name ends in "ix"
elif name[-2:] == "ix":
    print(name + parent + "x")
#checks if name ends in "o"
elif name[-1] in "o":
    print(name[:-1] + "ix" + parent + "x")
#otherwise, adds "ix"
else:
    print(name + "ix" + parent + "x")
