

n = int(input())  # The number of elements
a = list(map(int, input().split()))  # The elements
a.sort()

if n % 2 == 0:
    print(a[n // 2 - 1], a[n // 2])
else:
    print(a[n // 2])
