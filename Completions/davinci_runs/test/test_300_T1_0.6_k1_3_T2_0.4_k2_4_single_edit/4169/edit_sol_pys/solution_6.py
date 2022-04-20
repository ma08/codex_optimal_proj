

#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())  # a: cost, b: distance
    stores.append([a, b])

stores.sort(key=lambda x: x[0] / x[1])
#-----Solve-----

#-----Display-----
