
N = int(input())
for _ in range(N):
    line = input()
    if line.startswith("Simon says"):
        print(line[11:])
