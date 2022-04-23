n, k = map(int, input().split())

t = input()

ans = ""
for i in range(n):
    if i < k % n:  # k % n = k
        ans += t[i]
    else:
        ans += t[k % n]  # k % n = k

print(ans)
