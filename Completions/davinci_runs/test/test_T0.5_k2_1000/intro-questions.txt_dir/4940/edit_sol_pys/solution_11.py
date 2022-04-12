

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    times = [[int(i) for i in sys.stdin.readline().split()] for i in range(n)]
    mowers = [[i,j] for i in range(n) for j in range(m) if i != 0 or j != 0]
    mowers = sorted(mowers, key=lambda x: times[x[0]][x[1]])
    completed = [0]*n
    while len(mowers) > 0:
        mower = mowers.pop(0)
        if mower[1] == 0:
            completed[mower[0]] = times[mower[0]][0]
        else:
            completed[mower[0]] = max(completed[mower[0]], completed[mower[0]-1]) + times[mower[0]][mower[1]]
    print(' '.join([str(i) for i in completed]))

if __name__ == '__main__':
    main()
