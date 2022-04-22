

def main():
    num_ingredients = int(input())
    ingredients = list(map(int, input().split()))
    ingredients.sort()

    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2
        ingredients.pop(1)
        ingredients.sort()

    print(ingredients[0])
