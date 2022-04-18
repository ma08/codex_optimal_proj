

def main():
    n = int(input())
    ingredients = []

    min_diff = abs(ingredients[0][0] - ingredients[0][1])
    min_diff_ingredient = ingredients[0]

    for i in range(n):
        line = [int(x) for x in input().split()]
        ingredients.append(line)
        if abs(line[0] - line[1]) < min_diff:
            min_diff = abs(line[0] - line[1])
            min_diff_ingredient = line

    ingredients.sort()


    for i in range(1, n):
        if ingredients[i][0] > ingredients[i - 1][0]:
            if abs(ingredients[i][0] - ingredients[i][1]) < min_diff:
                min_diff = abs(ingredients[i][0] - ingredients[i][1])
                min_diff_ingredient = ingredients[i]

    print(min_diff_ingredient[0], min_diff_ingredient[1])

if __name__ == '__main__':
    main()
