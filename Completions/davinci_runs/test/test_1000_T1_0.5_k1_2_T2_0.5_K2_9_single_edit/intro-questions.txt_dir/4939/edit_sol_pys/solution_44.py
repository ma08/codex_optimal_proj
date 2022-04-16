

# Program starts here
n, k = map(int, input().split())  # n is the number of eggs and k is the number of commands
commands = input().split()  # commands is the list of commands

egg = 0  # egg is the total number of eggs

for i in range(len(commands)):  # loops through all the commands
    if "undo" in commands[i]:  # checks if the command is undo
        for j in range(int(commands[i][5:])):  # loops through the number of undo's
            if i - j - 1 >= 0:  # if the undo is not in the first command
                egg -= int(commands[i - j - 1])  # egg is subtracted by the number of undo's
            elif i - j - 1 < 0:  # if the undo is in the first command
                egg -= int(commands[0])  # egg is subtracted by the first command
    else:
        egg += int(commands[i])  # if the command is not undo, egg is added by the number of commands

print(egg % n)  # prints the total number of eggs modulo n
