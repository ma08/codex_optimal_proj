

n = int(input())
t = list(map(int, input().split()))[::-1]

# sort trees by time required for them to grow
# t.sort()

# find the earliest day when the party can be organized
day = 0
for i in range(n-1, -1, -1):
    if t[i] < day:
        day += 1
    day += t[i]

print(day)
