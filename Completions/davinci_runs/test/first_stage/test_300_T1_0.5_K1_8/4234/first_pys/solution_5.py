

n = int(input())
s = input()

i = 0
while i < n:
    if i % 2 == 0 and s[i] == s[i+1]:
        s = s[:i] + s[i+1:]
        n -= 1
        i -= 1
    else:
        i += 1

print(n - len(s))
print(s)