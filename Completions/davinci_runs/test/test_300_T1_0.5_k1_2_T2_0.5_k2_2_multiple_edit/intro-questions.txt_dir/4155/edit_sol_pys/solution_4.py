n = int(input())
a = list(map(int, input().split()))
a.sort()
ans = 0
for i in range(n):
    ans += a[i]
    if ans * 2 < a[i + 1]:
        print(i + 1)
        exit()
print(n)
