

def main(n, k, p):
    num_ingredients = n
    ingredients = list(map(int, k.split()))
    ingredients.sort(reverse=True)

    while len(ingredients) > 1:
        ingredients[0] = (ingredients[0] + ingredients[1]) / 2.0
        ingredients.pop(1)        
        ingredients.sort(reverse=True)

    print(ingredients[0] * p)

if __name__ == '__main__':
    n, k, p = input().split()
    main(int(n), k, int(p))
