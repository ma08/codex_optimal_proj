
# Solution

n = int(input())
s = input()

if s[0] == s[1]:
    r = 1
    t = s[0] + 'R'  # R
else:
    r = 0
    t = s[0]  # R

for i in range(1, n - 1):
    if s[i] == s[i + 1]:
        r += 1
        if s[i] == 'R':
            t += 'G'  # G
        elif s[i] == 'G':
            t += 'B'  # B
        else:
            t += 'R'  # R
    else:
        t += s[i]

t += s[-1]
print(r)
print(t)
