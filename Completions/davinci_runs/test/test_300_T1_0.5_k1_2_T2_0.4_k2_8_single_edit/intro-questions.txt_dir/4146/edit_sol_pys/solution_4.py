
n = int(input())
a = list(map(int, input().split()))

b = [0] * (10**5 + 1)
for i in a:
    b[i] += 1

a.sort()

ans = 0
if a[-1] == a[-2]:
    ans = 0
else:
    ans = a[-1] - a[-2]

print(ans)
