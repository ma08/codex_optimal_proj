

#!/usr/bin/env python
# -*- coding: utf-8 -*-

def main():
    N, M = map(int, input().split())
    A = []
    B = []
    for i in range(N):
        a, b = map(int, input().split())
        A.append(a)
        B.append(b)
    A = sorted(A)
    B = sorted(B)
    ans = 0
    for i in range(N):
        if B[i] <= M:
            M -= B[i]
            ans += A[i] * B[i]
        else:
            ans += A[i] * M
            M = 0
            break
    print(ans)

if __name__ == '__main__':
    main()