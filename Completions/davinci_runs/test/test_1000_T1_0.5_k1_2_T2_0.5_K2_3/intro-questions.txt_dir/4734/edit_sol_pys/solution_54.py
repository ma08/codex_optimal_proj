

# gets input and stores it in name and parent
name, parent = input().split() 

# checks if name ends in e, adds ex
if name[-1] == "e":
    print(name + "x" + parent)
# checks if name ends in ex, adds parent
elif name[-2:] == "ex":
    print(name + parent)
# checks if name ends in vowel
elif name[-1] in "aiou":
    print(name[:-1] + "ex" + parent)
# otherwise, adds ex and parent
else:
    print(name + "ex" + parent)
