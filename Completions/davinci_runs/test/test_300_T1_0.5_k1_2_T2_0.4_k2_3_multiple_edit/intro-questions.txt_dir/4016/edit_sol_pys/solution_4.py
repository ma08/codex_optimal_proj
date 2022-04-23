

n, k = map(int, input().split())
t = input()

ans = ""
for i in range(n):
    if i < k:
        ans += t[i]
    else:
        ans += t[k % n]

print(ans)
