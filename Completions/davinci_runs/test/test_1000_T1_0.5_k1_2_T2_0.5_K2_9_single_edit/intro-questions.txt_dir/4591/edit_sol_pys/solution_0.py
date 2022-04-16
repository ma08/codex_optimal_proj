

def pizza_at(a, b, c, x, y):
    return min(a * x + b * y, a * (x + y) + (x - (x + y) / 2) * a, b * (x + y) + (y - (x + y) / 2) * b, c * (x + y))

a, b, c, x, y = map(int, input().split())
print(pizza_at(a, b, c, x, y))
