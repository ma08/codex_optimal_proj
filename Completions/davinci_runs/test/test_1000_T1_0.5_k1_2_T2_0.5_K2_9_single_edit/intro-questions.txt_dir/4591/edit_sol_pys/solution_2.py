

def pizza_at(a, b, c, x, y):
    # If A is cheaper than B, buy as many A pizzas as possible, then buy B pizzas
    if a <= b: return b * y + a * x

    # If B is cheaper than A, buy as many B pizzas as possible, then buy A pizzas
    if b <= a: return a * x + b * y

    # If A and B are the same price, buy as many AB pizzas as possible, then buy A pizzas
    if a == b: return c * (x + y)

a, b, c, x, y = map(int, input().split())
print(pizza_at(a, b, c, x, y))
