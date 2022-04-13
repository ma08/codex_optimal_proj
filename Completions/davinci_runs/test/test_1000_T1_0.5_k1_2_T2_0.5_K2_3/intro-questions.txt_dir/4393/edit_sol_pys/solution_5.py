n = int(input())

s = input()

t = ''

for i in range(n):
    if s[i] != s[i-1]:
        t += s[i]

print(t)
