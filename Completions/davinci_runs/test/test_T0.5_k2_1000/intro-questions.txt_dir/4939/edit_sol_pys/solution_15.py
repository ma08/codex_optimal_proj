

import sys

def main():
    n = int(sys.stdin.readline())
    commands = sys.stdin.readline().split()
    current_child = 1
    undo_commands = []
    for command in commands:
        if command == 'undo':
            undo_commands.append(int(commands[commands.index(command)+1]))
        else:
            current_child += int(command)
    while undo_commands:
        undo_command = undo_commands.pop()
        undo_index = len(commands) - 1
        undo_commands_to_remove = []
        for i in range(undo_command):
            if commands[undo_index] == 'undo':
                undo_commands_to_remove.append(undo_index)
            else:
                current_child -= int(commands[undo_index])
        for i in undo_commands_to_remove:
            commands.pop(i+1)
        undo_index -= 1
    if current_child < 0:
        current_child += n
    elif current_child > n:
        current_child %= n
    print(current_child)

if __name__ == '__main__':
    main()
