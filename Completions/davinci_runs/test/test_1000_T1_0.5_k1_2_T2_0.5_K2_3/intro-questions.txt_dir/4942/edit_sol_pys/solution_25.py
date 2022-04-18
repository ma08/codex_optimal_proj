

n = int(input())
t = list(map(int, input().split()))

# sort trees by time required for them to grow
t.sort()

# find the earliest day when the party can be organized
day = 0
for i in range(n):
    day += max(t[i], day)

print(day)
