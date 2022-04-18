
import sys

def main():
    n, k = [int(i) for i in sys.stdin.readline().split()]
    commands = sys.stdin.readline().split()
    current_child = 0
    undo_commands = [0]
    for command in commands:
        if command == 'undo':
            undo_commands.append(int(commands[commands.index(command) + 1]))
        elif command == '0' or command == '-0':
            pass
        else:
            current_child += int(command)
    while undo_commands:
        undo_command = undo_commands.pop(0)
        undo_index = commands.index('undo') + 1
        undo_commands_to_remove = []
        for i in range(undo_command):
            try:
                if commands[undo_index] == 'undo':
                    undo_commands_to_remove.append(undo_index)
                else:
                    current_child -= int(commands[undo_index])
            except IndexError:
                undo_commands_to_remove.append(undo_index)
            undo_index += 1
        for i in undo_commands_to_remove:
            commands.pop(i - 1)
    if current_child < 0:
        current_child += n
    elif current_child > n:
        current_child %= n
    print(current_child)

if __name__ == '__main__':
    main()
