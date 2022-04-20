

def main():
    num_ingredients = int(input())  # number of ingredients
    ingredients = list(map(int, input().split()))  # list of ingredients
    ingredients.sort()  # sort the list of ingredients

    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2  # add the first two ingredients
        ingredients.pop(1)  # remove the first ingredient
        ingredients.sort()  # sort the list of ingredients

    print(ingredients[0])  # print the average

if __name__ == '__main__':
    main()
