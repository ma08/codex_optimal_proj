
def find_floor(n, x):
    floor = 0
    while n > 0:
        if floor != 0:
            if n > x:
                n -= x
            else:
                n -= 1
        floor += 1
    return floor

t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    print(find_floor(n, x))
