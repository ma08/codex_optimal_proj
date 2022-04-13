

# Solution

n = int(input())
t = list(map(int, input().split()))

t.sort()

maximum = t[0]
for i in range(1, n):
    if max < t[i]:
        max = t[i]
    t[i] = max + t[i]

print(t[-1] + 1)
