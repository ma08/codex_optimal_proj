
n = int(input())
t = list(input())
s = [0]*n
for i in range(n):
    s[i] = t[i]
    for j in range(i):
        if s[j] < s[i]:
            s[i] = t[i]
            break
print(''.join(s))
