
def find_floor(n, x):
    floor = 0
    while n > 0:
        if floor == 0:
            n -= 2
        else:
            n -= x
        floor += 1
    return floor


if __name__ == '__main__':
    t = int(input())

    for i in range(t):
        n, x = map(int, input().split())
        print(find_floor(n, x))
