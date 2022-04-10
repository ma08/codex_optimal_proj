

# SOLUTION

n = int(input())
a = list(map(int, input().split()))

if n == 2:
    print(2)
else:
    ans = 1
    c = 1
    for i in range(1, n):
        if a[i] > a[i - 1]:
            c += 1
        else:
            ans = max(ans, c)
            c = 1
    ans = max(ans, c)
    c = 1
    for i in range(1, n - 1):
        if a[i] > a[i - 1] and a[i] > a[i + 1]:
            c += 1
        else:
            ans = max(ans, c)
            c = 1
    ans = max(ans, c)
    print(ans)