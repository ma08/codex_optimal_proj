import math



def main():
    num_ingredients = int(input())  # number of ingredients
    ingredients = list(map(int, input().split()))  # list of ingredients
    ingredients.sort()  # sort ingredients

    while len(ingredients) > 1:  # while there are more than 1 ingredients
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2  # add smallest two ingredients and divide by 2
        ingredients.pop(1)  # delete second smallest ingredient
        ingredients.sort()  # sort ingredients

    print(math.floor(ingredients[0]))


if __name__ == '__main__':
    main()
