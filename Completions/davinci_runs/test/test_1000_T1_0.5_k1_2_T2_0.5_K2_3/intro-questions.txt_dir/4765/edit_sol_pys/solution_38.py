

def main():
    n = int(input())
    ingredients = []

    for i in range(n):
        ingredients.append([int(x) for x in input().split()])

    ingredients.sort(key=lambda x: x[0])

    minDiff = abs(ingredients[0][0] - ingredients[0][1])
    minDiffIngredient = ingredients[0][0]

    for i in range(1, n):
        diff = abs(ingredients[i][0] - ingredients[i][1])
        if diff < minDiff:
            minDiff = diff
            minDiffIngredient = ingredients[i][0]

    print(minDiff)

if __name__ == '__main__':
    main()
