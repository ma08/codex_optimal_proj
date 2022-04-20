
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    n, m = map(int, input().split())
    AB = [list(map(int, input().split())) for _ in range(m)]
    P = list(map(int, input().split()))

    res = 0
    for i in range(2 ** n):
        for j in range(m):
            cnt = 0
            for k in range(1, AB[j][0] + 1):
                if i & (1 << (AB[j][k] - 1)):
                    cnt += 1
            if cnt % 2 != P[j]:
                break
        else:
            res += 1
    print(res)


def main():
    resolve()


if __name__ == '__main__':
    main()
