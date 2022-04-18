import sys

def input():
    return sys.stdin.readline().rstrip()

def main():
    moves = input()
    res = []
    for i in range(len(moves)):
        if moves[i] == 'R':
            res.append('S')
        elif moves[i] == 'B':
            res.append('K')
        else:
            res.append('H')
    for i in range(len(moves) - 2):
        if moves[i] == 'R' and moves[i + 1] == 'B' and moves[i + 2] == 'L':
            res[i] = 'C'
            res[i + 1] = 'C'
            res[i + 2] = 'C'
    print(''.join(res))

if __name__ == '__main__':
    main()
