
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
    for j in range(len(moves)-2):
        if moves[j] == 'R' and moves[j+1] == 'B' and moves[j+2] == 'L':
            result[j] = 'C'
            result[j+1] = 'C'
            result[j+2] = 'C'
    print(''.join(result))

if __name__ == '__main__':
    main()
