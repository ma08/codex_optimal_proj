import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    moves = list(input())
    result = []
    for i in range(len(moves)):
        if moves[i] == 'R':
            result.append('S')
        elif moves[i] == 'B':
            result.append('K')
        else:
            result.append('H')
    for i in range(len(moves)-2):
        if moves[i] == 'R' and moves[i+1] == 'B' and moves[i+2] == 'R':
            result[i] = 'C'
            result[i+1] = 'C'
            result[i+2] = 'C'
    print(''.join(result))

if __name__ == '__main__':
    main()
