
def find_floors(n, x):
    floors = 0
    while n > 0:
        if floors == 0:
            n -= 2
        else:
            n -= x
        floors += 1

    return floors

t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    print(find_floors(n, x))
