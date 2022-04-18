import sys
from collections import Counter

n = int(input())
a_list = list(map(int, sys.stdin.readline().split()))

if len(Counter(a_list)) == n:
    print("YES")
else:
    print("NO")
