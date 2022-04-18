
n = int(input())
t = input()
s = t[0]
for i in range(n):
    if t[i] != s[-1]:
        s += t[i]

print(s)
