
import sys
sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7

N = int(input())
p = list(map(int, input().split()))


def resolve():
    res = 0
    for i in range(1, N):
        if p[i - 1] < p[i]:
            res += p[i] - p[i - 1]
    print(res)


if __name__ == '__main__':
    resolve()
