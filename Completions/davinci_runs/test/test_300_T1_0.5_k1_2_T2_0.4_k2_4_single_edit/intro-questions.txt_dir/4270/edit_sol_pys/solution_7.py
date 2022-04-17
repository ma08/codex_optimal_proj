

def main():
    num_ingredients = int(input())  # Number of ingredients
    ingredients = list(map(int, input().split()))  # List of ingredients
    ingredients.sort()  # Sort ingredients

    while len(ingredients) > 1:  # While there are more than one ingredients
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2  # Average first two ingredients
        ingredients.pop(1)  # Remove second ingredient
        ingredients.sort()  # Sort ingredients

    print(ingredients[0])  # Print final ingredient

if __name__ == '__main__':
    main()
