

n = int(input())
s = input()

c = [0] * n
res = 1
prev = s[0]
for i, v in enumerate(s):
    if v == prev:
        c[i] = c[i - 1]
    else:
        c[i] = c[i - 1] + 1
        res = c[i]
    prev = v


print(res)
print(*c)