

n = int(input())
t = input()

s = []

for i in range(n):
    s.insert(i, t[i])

for i in range(n, 1, -1):
    if n % i == 0:
        s = s[i-1::-1] + s[i:]
print(''.join(s))