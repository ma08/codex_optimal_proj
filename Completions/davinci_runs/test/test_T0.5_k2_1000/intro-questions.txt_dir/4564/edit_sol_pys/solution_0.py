# coding: utf-8

if __name__ == '__main__':
    N = int(input())
    A = list(map(int, input().split()))
    A.sort()
    print(A[-1] - A[0])
