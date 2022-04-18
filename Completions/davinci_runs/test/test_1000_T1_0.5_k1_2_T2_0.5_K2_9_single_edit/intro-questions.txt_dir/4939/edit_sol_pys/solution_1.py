

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
    undo_commands.sort(reverse=True)
    for undo_command in undo_commands:
        undo_index = commands.index('undo') - 1
        for i in range(undo_command + 1):
            undo_index -= 1
            current_child -= int(commands[undo_index])
        commands.pop(undo_index)
    if current_child < 0:
        current_child += n
    elif current_child > n:
        current_child %= n
    print(current_child)

if __name__ == '__main__':
    main()
