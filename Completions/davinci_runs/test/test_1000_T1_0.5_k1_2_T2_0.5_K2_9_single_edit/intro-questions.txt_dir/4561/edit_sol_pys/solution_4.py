import sys

x, a, b = map(int, input().split())

if a + b <= x:
    print("delicious")
elif a + b <= x + 1:
    print("safe")
else:
    print("dangerous")
