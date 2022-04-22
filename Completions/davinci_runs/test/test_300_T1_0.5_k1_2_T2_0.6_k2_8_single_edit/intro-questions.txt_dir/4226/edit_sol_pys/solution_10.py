# -----Answer-----
f = open("./file.txt", "r")
lines = f.readlines()


for line in lines:
    print(line, end="")
