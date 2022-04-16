

import sys
import math

def main():
    n = int(sys.stdin.readline())
    v = [int(x) for x in sys.stdin.readline().split()]
    if n == 1:
        print(0, v[0])
    elif n == 2:
        diff = abs(v[1] - v[0])
        print(1, v[1] + diff)
    elif n == 3:
        diff = abs(v[1] - v[0])
        ret_diff = abs(v[2] - v[1])
        if diff == ret_diff:
            print(2, v[2] + diff)
        else:
            print(-1)
    elif n > 3:
        diff = []
        ret_diff = []
        for i in range(n-1):
            diff.append(v[i+1] - v[i])
        for i in range(n-2):
            ret_diff.append(diff[i+1] - diff[i])
        if all(x == 0 for x in ret_diff):
            print(1, v[-1] + diff[0])
        elif all(x == 0 for x in diff):
            print(0, v[-1])
        else:
            print(2, v[-1] + diff[-1] + ret_diff[-1])

if __name__ == '__main__':
    main()
