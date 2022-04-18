

def main():
    num_ingredients = int(input())  # 2
    ingredients = list(map(int, input().split()))  # [4, 5]
    ingredients.sort()  # [4, 5]

    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2  # 4.5
        ingredients.pop(1)  # [4.5]
        ingredients.sort()  # [4.5]

    print(ingredients[0])

if __name__ == '__main__':
    main()
