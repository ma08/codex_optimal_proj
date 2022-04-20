

n = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

cur = n
t = 0
while cur > 0:
    t += 1
    cur -= min(cur, a)
    if cur <= 0:
        break
    cur -= min(cur, b)
    if cur <= 0:
        break
    cur -= min(cur, c)
    if cur <= 0:
        break
    cur -= min(cur, d)
    if cur <= 0:
        break
    cur -= min(cur, e)

print(t)