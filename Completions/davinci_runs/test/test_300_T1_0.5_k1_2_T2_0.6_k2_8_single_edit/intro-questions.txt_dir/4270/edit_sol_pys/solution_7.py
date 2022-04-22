

def main():
    num_ingredients = int(input())  # number of ingredients in the recipe
    ingredients = list(map(int, input().split()))  # the ingredients' weights
    ingredients.sort()  # sort the list in ascending order

    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)
        ingredients.sort()

    print(ingredients[0])

if __name__ == '__main__':
    main()
