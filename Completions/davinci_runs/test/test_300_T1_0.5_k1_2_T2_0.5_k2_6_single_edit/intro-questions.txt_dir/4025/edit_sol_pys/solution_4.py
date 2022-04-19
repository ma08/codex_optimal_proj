

def min_cost(x, y, a, b):
    if x > y:
        x, y = y, x
        a, b = b, a

    if x == 0:
        return y * b

    return min_cost(x, y % x, a, b) + (y//x) * a

x, y, a, b = [int(x) for x in input().split()]

print(min_cost(x, y, a, b))
