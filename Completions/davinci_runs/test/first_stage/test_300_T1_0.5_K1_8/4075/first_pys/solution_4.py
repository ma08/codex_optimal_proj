

# Solve using bitwise operation

import sys

def main():
    n, m = map(int, sys.stdin.readline().split())
    switches = [[] for i in range(m)]
    for i in range(m):
        tmp = list(map(int, sys.stdin.readline().split()))
        switches[i] = tmp[1:]
    p = list(map(int, sys.stdin.readline().split()))
    count = 0
    for i in range(1 << n):
        flag = True
        for j in range(m):
            c = 0
            for k in switches[j]:
                if i & (1 << (k - 1)):
                    c += 1
            if c % 2 != p[j]:
                flag = False
                break
        if flag:
            count += 1
    print(count)

if __name__ == '__main__':
    main()