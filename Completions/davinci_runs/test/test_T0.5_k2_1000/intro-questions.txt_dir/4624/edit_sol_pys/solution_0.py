

def find_floors(n, x, floors = 0):
    if n > 0:
        if floors == 0:
            return find_floors(n - 2, x, floors + 1)
        else:
            return find_floors(n - x, x, floors + 1)
    else:
        return floors

t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    print(find_floors(n, x))
