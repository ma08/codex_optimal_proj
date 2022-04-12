

def find_floor(n, x):  # n = no. of eggs, x = no. of floors
    floor = 0  # initial floor
    while n > 0:  # while eggs are left
        if floor == 0:  # if floor is 0
            n -= 2  # drop 2 eggs
        else:
            n -= x
        floor += 1
    return floor

t = int(input())

for i in range(t):
    n, x = map(int, input().split())
    print(find_floor(n, x))
