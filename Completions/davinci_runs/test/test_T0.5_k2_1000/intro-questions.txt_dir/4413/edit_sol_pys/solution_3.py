
# cook your dish here
for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    a.sort()
    ans = 1
    for i in range(1, n):
        if a[i]-a[i-1] == 1:
            ans += 1
    print(ans)
