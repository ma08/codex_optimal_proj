

n = int(input())
a = list(map(int, input().split()))

a_sorted = sorted(a)

if a == a_sorted:
    print(n)
else:
    print(n - 1)