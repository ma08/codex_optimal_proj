
N = int(input())
for i in range(N):
    command = input().split()
    if command[0] == "Simon" and command[1] == "says" and len(command) > 2:
        print(" ".join(command[2:]))
