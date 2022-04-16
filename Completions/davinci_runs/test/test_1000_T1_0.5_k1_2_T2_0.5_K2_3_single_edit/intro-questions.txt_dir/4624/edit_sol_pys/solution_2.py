
def find_floor(n, x):
    floor = 0
    while n > 0:
        if floor == 0:
            n -= 1
        else:
            n -= x
        floor += 1
    return floor

t = int(input())  # number of test cases

for i in range(t):
    n, x = map(int, input().split())  # n is number of eggs
    print(find_floor(n, x))
