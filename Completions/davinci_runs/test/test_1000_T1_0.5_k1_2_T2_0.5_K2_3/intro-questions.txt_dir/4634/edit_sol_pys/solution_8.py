

t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    left, right = 0, 0
    for i in range(n):
        if a[i] == 1:
            left = i + 1
            break
    for i in range(n-1, 0, -1):
        if a[i] == 1:
            right = i + 1
            break
    print(right-left - sum(a[left:right]))
