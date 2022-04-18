

n, k = map(int, input().split())
a = list(map(int, input().split()))

a_min = min(a)
a_max = max(a)

if k <= a_max - a_min:
    print(a_min + k)
else:
    print(a_max + k - (a_max - a_min))
