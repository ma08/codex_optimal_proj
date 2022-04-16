

def main():
    num_ingredients = int(input())  # Number of ingredients
    ingredients = list(map(int, input().split()))  # The ingredients
    ingredients.sort()  # Sort the ingredients
        # Add the first two ingredients together, divide by 2, and put it back in the list

        # Remove the second ingredient from the list
    while len(ingredients) > 1:
        # Sort the list again
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)
        ingredients.sort()

    print(ingredients[0])  # Print the first ingredient in the list

if __name__ == '__main__':
    main()
