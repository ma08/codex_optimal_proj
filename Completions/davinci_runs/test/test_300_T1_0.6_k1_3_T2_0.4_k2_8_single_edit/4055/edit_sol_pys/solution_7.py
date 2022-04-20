

n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]

if k == 1:
    print(0)
else:
    count = 0
    for i in range(1, n):
        if a[i] > a[i - 1]:
            count += 1

    print(count)
