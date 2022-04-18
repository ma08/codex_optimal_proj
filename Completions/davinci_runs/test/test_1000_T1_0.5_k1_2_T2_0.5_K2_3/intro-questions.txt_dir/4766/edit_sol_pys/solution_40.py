

N = int(input())
for i in range(N):
    line = raw_input()
    if line.startswith("Simon says "):
        print(line[11:])
