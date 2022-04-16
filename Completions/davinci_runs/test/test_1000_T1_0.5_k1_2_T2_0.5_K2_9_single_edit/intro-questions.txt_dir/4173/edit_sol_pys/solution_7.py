
q = int(input())

for i in range(q):
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    a.sort()
    min_diff = float('inf')
    for i in range(n-k):
        min_diff = min(min_diff, a[i+k-1] - a[i])

    print(min_diff)
