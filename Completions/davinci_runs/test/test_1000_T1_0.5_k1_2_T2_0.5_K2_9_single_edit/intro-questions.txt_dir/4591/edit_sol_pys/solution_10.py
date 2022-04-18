

import sys

def main():
    # Read input
    A, B, C, X, Y = [int(x) for x in sys.stdin.readline().split()]

        if X < Y:
            X, Y = Y, X

    # Calculate minimum cost
    cost = 0

    if A + B > 2 * C:
        # It is cheaper to buy two AB-pizzas and rearrange them into one A-pizza and one B-pizza
        if X > Y:
            # Buy AB-pizzas until X - Y = 0, then buy A-pizzas
            cost += 2 * C * Y
            X -= Y
            Y = 0
        else:
            # Buy AB-pizzas until Y - X = 0, then buy B-pizzas
            cost += 2 * C * X
            Y -= X
            X = 0

    # Buy remaining A-pizzas and B-pizzas
    cost += A * X
    cost += B * Y

    print(cost)

if __name__ == "__main__":
    main()
