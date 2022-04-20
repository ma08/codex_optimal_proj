

# Solution

n = int(input())
s = input()
t = input()

if s[0] == t[0] or s[1] == t[1]:
    print('NO')
else:
    print('YES')
    print(s[1] * n + s[0] * n + t[0] * n)