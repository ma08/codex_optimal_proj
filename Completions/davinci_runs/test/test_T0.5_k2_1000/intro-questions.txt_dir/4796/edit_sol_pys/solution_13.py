

def main():
    # Get the input.
    juice_amounts = list(map(int, input().split()))
    recipe_amounts = list(map(int, input().split()))
    # Compute the leftover juice amounts.
    leftover_amounts = [x - y for x, y in zip(juice_amounts, recipe_amounts)]  # noqa: E501
    # Output the results.
    for leftover_amount in leftover_amounts:
        print(round(leftover_amount, 6), end=' ')

if __name__ == '__main__':
    main()
