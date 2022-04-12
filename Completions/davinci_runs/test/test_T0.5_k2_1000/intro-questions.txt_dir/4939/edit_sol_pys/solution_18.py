
# Program starts here
n, k = map(int, input().split())
commands = input().split()

egg = 0  # initial egg

for i in range(len(commands)):
    if commands[i] == "undo":
        for j in range(int(commands[i + 1])):
            if i - j - 2 >= 0:
                egg -= int(commands[i - j - 2])
            elif i - j - 2 < 0:
                egg -= int(commands[0])
    else:
        egg += int(commands[i])

print(egg % n)
