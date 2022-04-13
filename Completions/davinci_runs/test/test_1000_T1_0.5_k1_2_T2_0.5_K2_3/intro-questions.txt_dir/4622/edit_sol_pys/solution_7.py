
import sys

n = int(input())
a_list = input().split()

if len(set(a_list)) == n:
    print("YES")
else:
    print("NO")
