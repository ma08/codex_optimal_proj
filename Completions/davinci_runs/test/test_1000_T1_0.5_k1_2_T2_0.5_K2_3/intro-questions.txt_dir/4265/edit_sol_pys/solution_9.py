s = input()
t = input()

ans = 0
for i, j in zip(s, t):
    if i != j:
        ans += 1

print(ans)
