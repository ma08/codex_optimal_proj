

#-----main-----
n, t = map(int, input().split())
cost = []
time = []

for i in range(n):
    c, ti = map(int, input().split())
    cost.append(c)
    time.append(ti)

if min(time) > t:
    print('TLE')
else:
    min_cost = 1000
    for i in range(n):
        if time[i] <= t:
            if min_cost > cost[i]:
                min_cost = cost[i]
    print(min_cost)