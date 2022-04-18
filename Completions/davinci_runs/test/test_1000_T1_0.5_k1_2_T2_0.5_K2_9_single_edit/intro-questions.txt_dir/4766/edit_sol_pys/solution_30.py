
for i in range(int(input())):
    line = input()
    if line.startswith("Simon says"):
        print(line[11:])
