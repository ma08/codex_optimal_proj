

import sys

def main():
    N, M = map(int, input().split())
    bulbs = [list(map(int, input().split())) for _ in range(M)]
    states = list(map(int, input().split())) 
    switches = [[False] * N for _ in range(M)]
    for i in range(M):
        for j in range(1, bulbs[i][0] + 1):
            switches[i][bulbs[i][j] - 1] = True
    #print(switches)
    cnt = 0
    for i in range(2 ** N):
        flag = True
        for j in range(M):
            c = 0
            for k in range(N):
                if switches[j][k] and ((i >> k) & 1):
                    c += 1
            if c % 2 != states[j]:
                flag = False
                break
        if flag:
            cnt += 1
    print(cnt)

if __name__ == '__main__':
    main()
