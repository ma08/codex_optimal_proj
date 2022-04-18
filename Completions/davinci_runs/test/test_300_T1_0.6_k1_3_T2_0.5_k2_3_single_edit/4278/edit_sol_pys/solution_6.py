
n = int(input())
a = [int(input()) for i in range(n)]
ans = 0
for i in range(n):
    for j in range(i+1, n):
        if a[i]==a[j]:
            ans += 1
print(ans)
