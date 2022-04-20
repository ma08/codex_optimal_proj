
n = int(input())
a = list(map(int, input().split()))
a.sort()
a.reverse()
print(a[0] * a[1])
