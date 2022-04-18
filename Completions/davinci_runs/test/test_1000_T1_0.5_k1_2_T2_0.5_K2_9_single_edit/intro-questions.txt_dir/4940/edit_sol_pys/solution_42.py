

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    times = [[int(i) for i in sys.stdin.readline().split()[1:]] for i in range(n)]
    swathers = [[i,j] for i in range(n) for j in range(m)]
    swathers = sorted(swathers, key=lambda x: times[x[0]][x[1]])
    completed = [0]*m
    while len(swathers) > 0:
        swather = swathers.pop(0)
        if swather[1] == 0:
            completed[swather[0]] = times[swather[0]][0]
        else:
            completed[swather[0]] = max(completed[swather[0]], completed[swather[0]-1]) + times[swather[0]][swather[1]]
    print(' '.join([str(i) for i in completed[1:]]))

if __name__ == '__main__':
    main()
