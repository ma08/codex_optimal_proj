

import sys

def main():
    n, m = map(int, input().split())
    switches = [list(map(int, input().split())) for _ in range(m)]
    states = list(map(int, input().split()))
    bulbs = [[False] * m for _ in range(n)]
    for i in range(m):
        for j in range(1, switches[i][0] + 1):
            bulbs[switches[i][j] - 1][i] = True
    # print(bulbs)
    cnt = 0
    for i in range(2 ** n):
        flag = True
        for j in range(m):
            c = 0
            for k in range(n):
                if bulbs[k][j] and ((i >> k) & 1):
                    c += 1
            if c % 2 != states[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
