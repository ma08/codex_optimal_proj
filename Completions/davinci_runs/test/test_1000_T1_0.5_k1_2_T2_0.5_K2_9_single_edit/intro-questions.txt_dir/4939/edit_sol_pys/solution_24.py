
sys.setrecursionlimit(10 ** 6)
import sys

def main():
    n, k = map(int, input().strip().split())
    commands = input().strip().split()
    print(calculate(n, k, commands))

def calculate(n, k, commands):
    if k == 0:
        return 0
    if commands[-1] == 'undo':
        return calculate(n, k - 1, commands[:-1])
    else:
        command = int(commands[-1])
        return (calculate(n, k, commands[:-1]) + command) % n

main()
