

# Solution

n = int(input())
s = input()
t = input()

ans = []
for i in range(n):
    if s[i] != t[i]:
        for j in range(i + 1, n):
            if s[j] == t[i]:
                ans += [j + 1]
                s = s[:j] + s[j - 1:j + 1] + s[j + 1:]
                break

if s == t:
    print(len(ans))
    print(*ans)
else:
    print(-1)