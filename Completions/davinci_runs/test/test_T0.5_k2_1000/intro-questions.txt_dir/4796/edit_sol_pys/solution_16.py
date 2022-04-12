

def main():
    # Get the input
    juice_amounts = list(map(int, input().split())) # Get the amounts of juice in the bottles
    recipe_amounts = list(map(int, input().split())) # Get the amounts of juice in the recipe
    # Compute the leftover juice amounts
    leftover_amounts = [x - y for x, y in zip(juice_amounts, recipe_amounts)] # Compute the leftover juice amounts
    # Output the results
    for leftover_amount in leftover_amounts: # Output the leftover juice amounts
        print(round(leftover_amount, 6), end=' ') # Output the leftover juice amounts

if __name__ == '__main__':
    main()
