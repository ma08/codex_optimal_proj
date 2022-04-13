# coding: utf-8

N = int(input())
A = [0] + list(map(int, input().split()))

ans = list(range(N + 1))
for i in range(1, N + 1):
    ans[A[i]] += 1

for i in range(1, N + 1):
    print(ans[i])
