n = int(input())
for i in range(n):
    line = input().strip()
    if line.startswith("Simon says"):
        print(line[11:])
