# -*- coding: utf-8 -*-

import sys

def main():
    n, m, c = map(int, input().split())
    b = list(map(int, input().split()))
    a = [list(map(int, input().split())) for i in range(n)]
    ans = 0
    for i in range(n): #iは行
        if sum(a[i][j]*b[j] for j in range(m)) + c > 0: #jは列
            ans += 1
    print(ans)

if __name__ == "__main__":
    main()
