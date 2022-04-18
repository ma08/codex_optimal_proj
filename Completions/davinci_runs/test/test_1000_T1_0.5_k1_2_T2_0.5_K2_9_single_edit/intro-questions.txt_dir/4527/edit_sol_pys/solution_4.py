

# Greedy Algorithm

t = int(input())

for _ in range(t):
    n = int(input())
    a = []
    for __ in range(n):
        a.append(list(map(int, input().split())))
    a.sort(key=lambda x: x[1])
    count = 0
    j = 0
    for i in range(n):
        if a[i][0] >= a[j][1]:
            count += 1
            j = i


# Binary Search

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    l = 0
    r = n - 1
    while l <= r:
        mid = (l + r) // 2
        if a[mid] == k:
            print(mid + 1)
            break
        elif a[mid] > k:
            r = mid - 1
        else:
            l = mid + 1
    else:
        print(-1)
    print(count)
