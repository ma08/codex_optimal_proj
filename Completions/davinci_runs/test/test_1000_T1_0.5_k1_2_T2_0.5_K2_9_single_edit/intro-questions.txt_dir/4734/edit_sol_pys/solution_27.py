

#gets input
name, parent = input().split(" ")

#checks if name ends in e
if name[-1] == "e":
    print(name + "ex" + parent)
#checks if name ends in ex
elif name[-2:] == "ex":
    print(name + parent)
#checks if name ends in vowel
elif name[-1] in "aiou":
    print(name[:-1] + "ex" + parent)
#otherwise, adds ex
else:
    print(name + "ex" + parent)
