# coding: utf-8

import sys

def main():
    n = int(sys.stdin.readline().rstrip())
    a = list(map(int, sys.stdin.readline().rstrip().split()))
    ans = 1  # 最小公倍数
    for i in range(n):
        ans *= a[i]  # ansにa[i]をかける
        if ans > 10 ** 18:
            print(-1)
            return
    print(ans)

if __name__ == '__main__':

    main()
