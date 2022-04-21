
n = int(input())
s = str(input())
k = str(input())
for i in range(n):
    if s[i] == k:
        s = s[:i] + s[i+1:]
print(s)
