

import sys

def main():
    n, m = [int(i) for i in sys.stdin.readline().split()]
    times = [[int(i) for i in sys.stdin.readline().split()] for i in range(n)]
    shearers = [[i,j] for i in range(n) for j in range(m-1)]
    shearers = sorted(shearers, key=lambda x: times[x[0]][x[1]+1])
    completed = [0]*n
    while len(shearers) > 0:
        shearer = shearers.pop(0)
        if shearer[1] == m-2:
            completed[shearer[0]] = times[shearer[0]][m-1]
        else:
            completed[shearer[0]] = max(completed[shearer[0]], completed[shearer[0]-1]) + times[shearer[0]][shearer[1]+1]
    print(' '.join([str(i) for i in completed]))

if __name__ == '__main__':
    main()
