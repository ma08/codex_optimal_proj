

#Program
n, k = map(int, input().split())
children = [0] * n
children[0] = 1

for i in range(k):
    command = input()
    if command[0:4] == "undo":
        command = command.split()
        for j in range(int(command[1])):
            children[j] = 0
    else:
        command = int(command)
        if command < 0:
            children[(command % n) + n] = 1
        else:
            children[command % n] = 1
for i in range(n):
    if children[i] == 1:
        print(i)
        break
