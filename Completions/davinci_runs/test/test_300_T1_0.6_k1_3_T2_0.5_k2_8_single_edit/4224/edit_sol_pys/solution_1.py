# -*- coding: utf-8 -*-

def main():
    N = int(input())
    A = [int(a) for a in input().split()]
    ans = 0
    while all(a % 2 == 0 for a in A):
        cnt = 0
        for i in range(N):
            if A[i] % 2 == 0:
                A[i] //= 2
                cnt += 1
        ans += 1
    print(ans)

if __name__ == '__main__':
    main()
