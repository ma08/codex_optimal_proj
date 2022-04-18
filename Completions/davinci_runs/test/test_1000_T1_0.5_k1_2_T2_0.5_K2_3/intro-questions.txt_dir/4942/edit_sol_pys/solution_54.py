
#
# Solution

n = int(input())
t = list(map(int, input().split()))

t.sort()

max = t[0]
for i in range(1, n):
    if max < t[i]:
        max = t[i]
    t[i] += max

print(t[-1] + 1)
