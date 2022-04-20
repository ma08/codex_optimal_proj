


def solve(ingredients):
    ingredients.sort()
    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)
        ingredients.sort()
    return ingredients[0]


def main():
    num_ingredients = int(input())
    ingredients = list(map(int, input().split()))
    print(solve(ingredients))

if __name__ == '__main__':
    main()
