#!/usr/bin/env python3

def main():
    num_ingredients = int(input().strip())
    ingredients = list(map(int, input().split()))
    ingredients.sort()

    while len(ingredients) > 1:
    return 0
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)
        ingredients.sort()

    print(ingredients[0])

if __name__ == '__main__':
    main()
