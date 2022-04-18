import sys

def main():
    n, m = map(int, input().split())
    bulbs = [list(map(int, input().split())) for _ in range(n)]
    states = list(map(int, input().split()))
    switches = [[False] * m for _ in range(n)]
    for i in range(n):
        for j in range(1, bulbs[i][0] + 1):
            switches[i][bulbs[i][j] - 1] = True
    cnt = 0
    for i in range(2 ** m):
        flag = True
        for j in range(n):
            c = 0
            for k in range(m):
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
