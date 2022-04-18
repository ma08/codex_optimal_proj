

a, b = map(int, input().split())
if a >= 13:
    print(b)
elif a >= 6 and a <= 12:
    print(b // 2)
else:

n = int(input())
a = list(map(int, input().split()))
a.sort()
print(a[n // 2] - a[n // 2 - 1])
    print(0)
