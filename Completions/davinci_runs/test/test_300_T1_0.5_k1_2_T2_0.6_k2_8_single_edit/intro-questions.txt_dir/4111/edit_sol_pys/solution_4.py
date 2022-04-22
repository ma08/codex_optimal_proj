n = int(input())
s = list(map(int, input().split()))


sum_ = sum(s)
c = 0
t = 0
for i in range(n):
    t += s[i]
    if t == sum_ / 2:
        c += 1
        t = 0

print(c)
