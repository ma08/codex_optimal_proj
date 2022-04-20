
import math
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split()) #n is number of stores, m is number of houses
stores = [] #stores[i] = [distance, cost]
houses = [] #houses[i] = distance

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b]) #stores[i] = [distance, cost]

for i in range(m):
    c = int(input())
    houses.append(c) #houses[i] = distance

#for each house, find the closest store
#for each house, find the cheapest store
#for each house, find the cheapest store within range

#for each store, find the closest house
#for each store, find the house that needs the least amount of items
#for each store, find the house that needs the least amount of items within range


#find the closest store to each house
for house in houses:
    min_dist = math.inf
    for store in stores:
        dist = abs(house - store[0])
        if dist < min_dist:
            min_dist = dist
    print(min_dist)
#-----Solve-----

#-----Display-----
