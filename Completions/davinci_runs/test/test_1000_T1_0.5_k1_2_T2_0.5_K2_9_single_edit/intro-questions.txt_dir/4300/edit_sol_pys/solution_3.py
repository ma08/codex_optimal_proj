#! /usr/bin/env python3

N = int(input())
d = list(map(int, input().split()))

print(sum([d[i]*d[j] for i in range(N) for j in range(i+1, N)]))
