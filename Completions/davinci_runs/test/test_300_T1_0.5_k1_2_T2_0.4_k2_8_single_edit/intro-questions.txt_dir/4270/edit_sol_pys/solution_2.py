

def main():
    num_ingredients = int(input()) # Get the number of ingredients
    ingredients = list(map(int, input().split())) # Get the ingredients
    ingredients.sort() # Sort the ingredients

    while len(ingredients) > 1: # While the list of ingredients is not empty
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2 # Calculate the new ingredient
        ingredients.pop(1) # Remove the second ingredient
        ingredients.sort() # Sort the ingredients again

    print(ingredients[0]) # Print the remaining ingredient

if __name__ == '__main__':
    main()
