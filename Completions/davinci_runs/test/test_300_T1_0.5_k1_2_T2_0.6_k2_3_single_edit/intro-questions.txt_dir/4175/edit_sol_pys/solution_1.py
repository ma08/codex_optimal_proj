n = int(input())
s = [input() for i in range(n)]
for i in range(1, n):
    if s[i][0] != s[i - 1][-1] or s[i] in s[:i]:
        print("No")
        break
else:
    print("Yes")
