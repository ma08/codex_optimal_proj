
#!/usr/bin/python3
# -*- coding: utf-8 -*-

# Number of teams
N = int(input())
# Time required for the i-th team to understand and implement the algorithm
T = list(map(int, input().split()))

# Sorted times
T.sort()

total_time = 0
for i in range(N):
    total_time += T[i] * (N - i)

print(total_time)
