import sys

n = int(input())
a_list = list(map(int, input().split()))

if len(set(a_list)) == n:
    print("YES")
else:
    print("NO")
