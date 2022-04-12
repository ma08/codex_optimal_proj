

import sys

def main():
    n, k = [int(i) for i in sys.stdin.readline().split()]
    commands = sys.stdin.readline().split()
    current_child = 0
    undo_commands_to_remove = 0
    for command in commands:
        if command == 'undo':
            undo_commands_to_remove += int(commands[commands.index(command)+1])
        elif command == '0' or command == '-0':
            pass
        else:
            current_child += int(command)
    while undo_commands_to_remove > 0:
        undo_command = undo_commands_to_remove
        undo_commands_to_remove = 0
        undo_index = commands.index('undo')
        for i in range(undo_command):
            undo_index -= 1
            if commands[undo_index] == 'undo':
                undo_commands_to_remove += int(commands[undo_index+1])
            else:
                current_child -= int(commands[undo_index])
    if current_child < 0:
        current_child += n
    elif current_child > n:
        current_child %= n
    print(current_child)

if __name__ == '__main__':
    main()
