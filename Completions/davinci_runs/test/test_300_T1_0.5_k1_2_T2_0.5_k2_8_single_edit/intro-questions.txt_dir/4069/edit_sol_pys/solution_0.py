
n = int(input())
s = input()
 
ans = 0
for i in range(1, n):
    t = set(s[:i])
    for j in s[i:]:
        if j in t:
            ans = max(ans, len(t))
            break
        t.add(j)
    else:
        ans = max(ans, len(t))
 
print(ans)
