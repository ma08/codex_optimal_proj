
import sys

def main():
    n, k = [int(i) for i in sys.stdin.readline().strip().split()]
    commands = sys.stdin.readline().split()
    current_child = 0
    undo_commands = []
    for command in commands:
        if command == 'undo':
            undo_commands.append(int(commands[commands.index(command)+1]))
        else:
            current_child += int(command) % n
    for undo_command in undo_commands:
        for i in range(undo_command):
            current_child -= int(commands[commands.index('undo') - 1 - i])
        commands = commands[:commands.index('undo') - undo_command]
    current_child %= n
    print(current_child)

if __name__ == '__main__':
    main()
