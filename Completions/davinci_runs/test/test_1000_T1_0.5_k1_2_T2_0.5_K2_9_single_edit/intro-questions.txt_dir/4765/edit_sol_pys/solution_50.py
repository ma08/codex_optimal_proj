

def main():
    n = int(input())
    ingredients = []

    for i in range(n):
        ingredients.append([int(x) for x in input().split()])

    ingredients.sort(key=lambda x: x[0])

    min_diff = abs(ingredients[0][0] - ingredients[0][1])
    min_diff_ingredient = ingredients[0]

    for i in range(1, n):
        if ingredients[i][0] > ingredients[i - 1][0]:
            diff = abs(ingredients[i][0] - ingredients[i][1])
            if diff < min_diff:
                min_diff = diff
                min_diff_ingredient = ingredients[i]

    print(min_diff)

if __name__ == '__main__':
    main()
