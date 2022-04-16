
#gets input
name, parent = input().split(" ")

#checks if name ends in e
if name[-1] == "e" or name[-1] == "E":
    print(name + "x" + " " + parent)
#checks if name ends in ex
elif name[-2:] == "ex" or name[-2:] == "Ex":
    print(name + " " + parent)
#checks if name ends in vowel
elif name[-1] in "aiouAIOU":
    print(name[:-1] + "ex" + " " + parent)
#otherwise, adds ex
else:
    print(name + "ex" + " " + parent)
