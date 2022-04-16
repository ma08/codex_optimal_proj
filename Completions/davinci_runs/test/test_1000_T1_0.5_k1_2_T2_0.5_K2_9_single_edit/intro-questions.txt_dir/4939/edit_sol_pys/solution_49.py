

#Program starts here
n, k = map(int, input().split())
commands = input().split()

egg = 0

for i in range(k):
    if "undo" in commands[i]:
        for j in range(int(commands[i][5:])):
            if i - j - 1 >= 0:
                egg -= int(commands[i-j-1])
            elif i - j - 1 < 0:
                egg -= int(commands[0])
    else:
        egg += int(commands[i])

print(egg % n)
