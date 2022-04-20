

import sys

def main():
    N, M = map(int, sys.stdin.readline().split())

    bulbs = []
    for i in range(M):
        bulbs.append(list(map(int, sys.stdin.readline().split())))

    p = list(map(int, sys.stdin.readline().split()))

    ans = 0

    # bit全探索
    for i in range(2**N):
        lit = 0
        for j in range(M):
            cnt = 0
            for k in range(1, len(bulbs[j])):
                if (i>>(bulbs[j][k]-1))&1:
                    cnt += 1
            if cnt % 2 == p[j]:
                lit += 1
        if lit == M:
            ans += 1

    print(ans)

if __name__ == '__main__':
    main()