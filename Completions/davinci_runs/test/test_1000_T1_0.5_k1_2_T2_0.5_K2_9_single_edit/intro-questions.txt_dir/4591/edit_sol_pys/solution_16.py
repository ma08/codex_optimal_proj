

def pizza_at(a, b, c, x, y, z):
    # If A is cheaper than B, buy as many A pizzas as possible
    if a <= b:
        # If there are still more A pizzas needed, buy AB pizzas
        if x > z:
            # If AB is cheaper than A, buy AB pizzas
            if a < c:
                return a * (x + y) + (x - z) * a
            # If AB is more expensive than A, buy A pizzas
            else:
                return c * (x + y)
        # If there are no more A pizzas needed, buy B pizzas
        else:
            return b * y + a * x

    # If B is cheaper than A, buy as many B pizzas as possible
    else:
        # If there are still more B pizzas needed, buy AB pizzas
        if y > z:
            # If AB is cheaper than B, buy AB pizzas
            if b < c:
                return b * (x + y) + (y - z) * b
            # If AB is more expensive than B, buy B pizzas
            else:
                return c * (x + y)
        # If there are no more B pizzas needed, buy A pizzas
        else:
            return a * x + b * y

a, b, c, x, y, z = map(int, input().split())
print(pizza_at(a, b, c, x, y, z))
