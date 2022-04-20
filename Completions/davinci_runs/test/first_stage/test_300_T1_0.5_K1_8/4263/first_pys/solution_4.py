

s = input()

ans = 0

for i in range(len(s)):
    for j in range(i, len(s)):
        if len(set(s[i:j+1]) - set('ACGT')) == 0:
            ans = max(ans, j-i+1)

print(ans)