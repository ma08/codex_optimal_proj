# coding: utf-8

a, b, c = list(map(int, input().split()))

if (a == b) and (a != c):
    print("Yes")
elif (a == c) and (a != b):
    print("Yes")
elif (b == c) and (b != a):
    print("Yes")
else:
    print("No")
