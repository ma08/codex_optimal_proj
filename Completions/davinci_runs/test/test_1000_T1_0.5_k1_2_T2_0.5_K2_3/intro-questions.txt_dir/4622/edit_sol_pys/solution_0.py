import sys

n = int(input())
a_list = list(map(int, sys.stdin.readline().split()))[:n]

if len(set(a_list)) == n:
    print("YES")
else:
    print("NO")
