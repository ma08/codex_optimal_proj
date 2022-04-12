import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
c = list(map(int, input().split()))
a.sort()
b.sort()
c.sort()
print(a)
print(b)
print(c)
