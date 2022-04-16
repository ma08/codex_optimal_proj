

def find_floor(n, x, y):
    floor = 0
    while n > 0:
        if floor == y:
            n -= x - 1
        n -= 1
        floor += 1
    return floor

t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    print(find_floor(n, x))
