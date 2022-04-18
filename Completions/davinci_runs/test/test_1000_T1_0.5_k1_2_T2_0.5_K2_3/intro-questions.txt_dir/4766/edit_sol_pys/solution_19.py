n = int(input())
for i in range(n):
    line = input()
    if line.startswith("Simon says "):
        print(line[11:])

N = int(input())
for i in range(N):
    line = input()
    if line.startswith("simon says "):
        print(line[11:])
