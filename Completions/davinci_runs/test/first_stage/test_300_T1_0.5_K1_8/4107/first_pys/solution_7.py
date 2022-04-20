
n, k = map(int, input().split())
s = input()

# 1. find all the spots for routers
# 2. sort them by the cost of connecting directly to the internet
# 3. check if the spot is within the range of the previous router
# 4. if no, connect directly to the internet
# 5. if yes, skip
# 6. add the cost of connecting directly to the internet

spots = []
total_cost = 0

for i in range(n):
    if s[i] == '1':
        spots.append(i+1)
    else:
        total_cost += (i+1)

spots.sort()

last_router_range = 0

for i in range(len(spots)):
    if spots[i] > last_router_range:
        total_cost += spots[i]
        last_router_range = spots[i] + k

print(total_cost)