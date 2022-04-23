


#-----Functions-----
def sort_stores(stores):
    return sorted(stores, key=lambda x: x[0])
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []

for i in range(n):
    a, b = map(int, input().split())
    stores.append([a, b])
stores = sort_stores(stores)


#-----Solve-----

#-----Display-----
