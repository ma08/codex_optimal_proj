

# Solution 1

n = int(input())
t = list(map(int, input().split()))

t.sort()

maximum = t[0]
for i in range(1, n):
    if maximum < t[i]:
        maximum = t[i]
    t[i] = maximum + t[i]

print(t[-1] + 1)
