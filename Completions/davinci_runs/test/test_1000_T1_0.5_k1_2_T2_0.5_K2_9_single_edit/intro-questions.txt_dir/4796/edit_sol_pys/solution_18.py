

def main():
    # Get the input
    juice_amounts = list(map(int, input().split()))
    recipe_amounts = list(map(int, input().split()))
    # Compute the left over juice amounts
    leftover_amounts = [x - y for x, y in zip(juice_amounts, recipe_amounts)]
    # Output the result
    for leftover_amount in leftover_amounts:
        print(round(leftover_amount, 6), end=' ')

if __name__ == '__main__':
    main()
