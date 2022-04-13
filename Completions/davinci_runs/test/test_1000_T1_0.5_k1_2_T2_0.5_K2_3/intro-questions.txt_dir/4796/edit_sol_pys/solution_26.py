

def main():
    # Get the input
    juice_amounts = list(map(int, input().split()))
    recipe_amounts = list(map(int, input().split()))
    # Compute the left over juice amounts
    left_over_amounts = [x - y for x, y in zip(juice_amounts, recipe_amounts)
    # Output the results
    for left_over_amount in left_over_amounts:
        print(round(left_over_amount, 6), end=' ')]

if __name__ == '__main__':
    main()
