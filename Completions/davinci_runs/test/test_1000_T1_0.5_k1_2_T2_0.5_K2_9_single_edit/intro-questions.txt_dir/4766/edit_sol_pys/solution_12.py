
n = int(input())
for i in range(n):
    line = input()
    if line.startswith("Simon says"):
        print(line[11:])
