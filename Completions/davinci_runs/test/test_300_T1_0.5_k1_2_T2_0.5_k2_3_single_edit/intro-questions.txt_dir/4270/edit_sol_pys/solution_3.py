
def main():
    num_ingredients = int(input())
    ingredients = sorted(map(int, input().split()))

    while len(ingredients) > 1:

        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)

    print(ingredients[0])

if __name__ == '__main__':
    main()
