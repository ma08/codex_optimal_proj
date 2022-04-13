
n = int(input())
t = list(map(int, input().split()))

t.sort()

day = 0
for i in range(n):
    if t[i] < day:
        day += 1
    else:
        day += t[i]

print(day)
