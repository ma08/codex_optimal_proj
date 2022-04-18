
# Solution

n = int(input())
s = input()

if s[0] == s[1]:
    r = 1
    t = s[0] + 'R'
else:
    r = 0
    t = s[0]

for i in range(1, n - 1):
    if s[i] == s[i + 1]:
        r += 1
        if s[i] == 'R':
            t += 'G'
        elif s[i] == 'G':
            t += 'B'
        else:
            t += 'R'
    else:
        t += s[i]

t += s[-1]
print(r)
print(t)
