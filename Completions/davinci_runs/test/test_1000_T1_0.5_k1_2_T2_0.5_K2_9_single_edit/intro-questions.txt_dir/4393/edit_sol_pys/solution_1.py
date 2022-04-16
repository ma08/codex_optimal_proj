

n = int(input())

t = input()

s = []

for i in range(n):
    if t[i] != t[i-1] or i == 0:
        s.append(t[i])

print(''.join(s))
