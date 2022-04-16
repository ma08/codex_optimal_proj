

N = int(input().strip())
for i in range(N):
    line = input().strip()
    if line.startswith("Simon says"):
        print(line[11:])
