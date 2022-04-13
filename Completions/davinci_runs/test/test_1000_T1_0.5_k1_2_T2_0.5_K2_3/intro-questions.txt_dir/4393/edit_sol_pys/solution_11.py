n = int(input())
t = input()
ans = t[0]
for i in range(1, n):
    if t[i] != t[i - 1]:
        ans += t[i]
print(ans)
