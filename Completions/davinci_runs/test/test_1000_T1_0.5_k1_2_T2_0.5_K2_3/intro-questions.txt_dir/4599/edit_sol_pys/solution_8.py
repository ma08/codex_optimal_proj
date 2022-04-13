n = int(input())
a = list(map(int, input().split()))
a = sorted(a, reverse=True)
print(sum(a[::2]) - sum(a[1::2]))
