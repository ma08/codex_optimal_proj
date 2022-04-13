
n = int(input())

t = input()

s = []

for i in range(n):
    if i == 0 or t[i] != t[i-1]:
        s.append(t[i])

print(''.join(s))
