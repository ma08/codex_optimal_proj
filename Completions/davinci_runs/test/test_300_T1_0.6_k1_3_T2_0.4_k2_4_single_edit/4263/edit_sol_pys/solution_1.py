

s = input() 
n = len(s) 
ans = 0
for i in range(n):
    for j in range(i+1, n+1):
        if "A" in s[i:j] and "C" in s[i:j] and "G" in s[i:j] and "T" in s[i:j]:
            ans = max(ans, j-i)
print(ans)
