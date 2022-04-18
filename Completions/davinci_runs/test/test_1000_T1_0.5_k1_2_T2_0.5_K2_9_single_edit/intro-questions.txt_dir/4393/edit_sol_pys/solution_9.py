

n = int(input())
t = input()

s = t[0]
for i in range(n):
    if s[-1] != t[i]:
        s += t[i]

print(s)
