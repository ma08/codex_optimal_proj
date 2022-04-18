
import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    moves = input()
    result = []
    for i in range(len(moves)):
        if moves[i] == 'R':
            result.append('S')
        elif moves[i] == 'B':
            result.append('K')
        else:
            result.append('H')
    for i in range(len(moves)-1):
        if moves[i] == 'R' and moves[i+1] == 'L':
            result[i] = 'C' if result[i] == 'S' else 'S'
            result[i+1] = 'C' if result[i+1] == 'S' else 'S'
    print(''.join(result))

if __name__ == '__main__':
    main()
