
n, k = map(int, input().split())
t = input()

ans = ""
for i in range(n):
    ans += t[(i + (k - 1)) % n]

print(ans)
