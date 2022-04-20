
INF = 1000000007
#-----Constants-----

#-----Input and Setup-----
n, m = map(int, input().split())
stores = []
storedict = {}
for i in range(n):
    a, b = map(int, input().split())
    storedict[a] = b
    stores.append([a, b])

def solve(n, m, stores):
    for i in range(m):
        a, b = map(int, input().split())
        if a in storedict:
            storedict[a] += b
        else:
            storedict[a] = b
    max_val = 0
    for key, val in storedict.items():
        max_val = max(max_val, val)
    return max_val
#-----Solve-----

print(solve(n, m, stores))
#-----Display-----
