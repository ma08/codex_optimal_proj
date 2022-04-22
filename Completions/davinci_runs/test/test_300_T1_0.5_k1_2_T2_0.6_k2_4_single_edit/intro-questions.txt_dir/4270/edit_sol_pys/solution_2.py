
def main():
    num_ingredients = int(input())
    ingredients = list(map(float, input().split()))
    ingredients.sort()

    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)
        ingredients.sort()

    print("{0:.2f}".format(ingredients[0]))

if __name__ == '__main__':
    main()
