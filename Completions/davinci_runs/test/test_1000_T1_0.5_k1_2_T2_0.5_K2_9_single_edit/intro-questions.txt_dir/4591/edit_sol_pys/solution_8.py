

def main():
    a, b, c, x, y = map(int, input().split())
    # If A is cheaper than B, buy as many A pizzas as possible
    if a <= b:
        # If there are still more A pizzas needed, buy AB pizzas
        if x > (x + y) / 2:
            # If AB is cheaper than A, buy AB pizzas
            if a < c:
                print(a * (x + y) + (x - (x + y) / 2) * a)
            # If AB is more expensive than A, buy A pizzas
            else:
                print(c * (x + y))
        # If there are no more A pizzas needed, buy B pizzas
        else:
            print(b * y + a * x)
    # If B is cheaper than A, buy as many B pizzas as possible
    else:
        # If there are still more B pizzas needed, buy AB pizzas
        if y > (x + y) / 2:
            # If AB is cheaper than B, buy AB pizzas
            if b < c:
                print(b * (x + y) + (y - (x + y) / 2) * b)
            # If AB is more expensive than B, buy B pizzas
            else:
                print(c * (x + y))
        # If there are no more B pizzas needed, buy A pizzas
        else:
            print(a * x + b * y)
if __name__ == '__main__':
    main()
