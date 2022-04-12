

import sys

def main():
    n, k = [int(i) for i in sys.stdin.readline().split()]
    commands = sys.stdin.readline().split()
    current_child = 0
    undo_commands_to_remove = []
    for command in commands:
        if command == 'undo':
            undo_commands_to_remove.append(int(commands[commands.index(command)+1]))
        elif command == '0' or command == '-0' or command == '0\n' or command == '-0\n':
            pass
        else:
            current_child += int(command)
    while undo_commands_to_remove:
        undo_command = undo_commands_to_remove.pop()
        undo_index = commands.index('undo')
        undo_commands_to_remove_to_remove = []
        for i in range(undo_command):
            undo_index -= 1
            if commands[undo_index] == 'undo':
                undo_commands_to_remove_to_remove.append(undo_index)
            else:
                current_child -= int(commands[undo_index])
        for i in undo_commands_to_remove_to_remove:
            commands.pop(i)
    if current_child < 0 or current_child > n:
        current_child = current_child % n
    print(current_child)

if __name__ == '__main__':
    main()
