
import sys

def main():
    n, k = [int(i) for i in sys.stdin.readline().split()] #read the first line
    commands = sys.stdin.readline().split() #read the second line
    current_child = 0
    undo_commands = [] #list to store undo commands
    for command in commands:
        if command == 'undo': #add undo commands to the list
            undo_commands.append(int(commands[commands.index(command)+1])) #add the undo amount to the list
        elif command == '0' or command == '-0': #ignore 0 or -0
            pass
        else: #add the command to the current position
            current_child += int(command)
    while undo_commands: #loop while undo commands are left
        undo_command = undo_commands.pop() #get the last undo command
        undo_index = commands.index('undo') #get the last undo command index
        undo_commands_to_remove = [] #list to store undo commands to be removed
        for i in range(undo_command): #loop undo_command times
            undo_index -= 1 #decrement the index
            if commands[undo_index] == 'undo': #if the command is undo add it to the list
                undo_commands_to_remove.append(undo_index) #add the index to the list
            else:
                current_child -= int(commands[undo_index]) #subtract the command from the current position
        for i in undo_commands_to_remove: #loop through the undo commands to remove
            commands.pop(i) #remove the undo command from the list
    if current_child < 0: #if the current position is less than 0
        current_child += n #add n to current position
    elif current_child > n: #if the current position is greater than n
        current_child %= n #mod n from current position
    print(current_child) #print the current position

if __name__ == '__main__':
    main()
