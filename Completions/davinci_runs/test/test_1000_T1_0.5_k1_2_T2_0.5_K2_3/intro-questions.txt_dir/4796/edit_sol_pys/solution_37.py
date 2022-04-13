
def main():
    # Get the input.
    juice_amounts = list(map(int, input().split())) # Split the input into a list.
    recipe_amounts = list(map(int, input().split())) # Split the input into a list.
    # Compute the leftover juice amounts.
    leftover_amounts = [x - y for x, y in zip(juice_amounts, recipe_amounts)] # Compute the leftover juice amounts.
    # Output the results.
    for leftover_amount in leftover_amounts: # Output the results.
        print(round(leftover_amount, 6), end=' ') # Output the results.

if __name__ == '__main__':
    main()
