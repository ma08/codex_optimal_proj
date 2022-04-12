

def pizza_at(a, b, c, x, y):
    # If A is cheaper than B, buy as many A pizzas as possible.
    if a <= b:
        # If there are still more A pizzas needed, buy AC pizzas.
        if x > (x + y) / 2:
            # If AC is cheaper than A, buy AC pizzas.
            if a < c:
                return a * (x + y) + (x - (x + y) / 2) * a
            # If AC is more expensive than A, buy A pizzas.
            else:
                return c * (x + y)
        # If there are no more A pizzas needed, buy B pizzas.
        else:
            return b * y + a * x

    # If B is cheaper than A, buy as many B pizzas as possible.
    else:
        # If there are still more B pizzas needed, buy BC pizzas.
        if y > (x + y) / 2:
            # If BC is cheaper than B, buy BC pizzas.
            if b < c:
                return b * (x + y) + (y - (x + y) / 2) * b
            # If AB is more expensive than B, buy B pizzas.
            else:
                return c * (x + y)
        # If there are no more B pizzas needed, buy A pizzas.
        else:
            return a * x + b * y

a, b, c, x, y = map(int, input().split())
print(pizza_at(a, b, c, x, y))
