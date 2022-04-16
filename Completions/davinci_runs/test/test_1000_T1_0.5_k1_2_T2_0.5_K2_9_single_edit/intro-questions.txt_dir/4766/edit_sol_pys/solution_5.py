
N = int(input())
for i in range(N):
    line = input()
    if line.startswith("Simon says"):
        print(line[10:])
