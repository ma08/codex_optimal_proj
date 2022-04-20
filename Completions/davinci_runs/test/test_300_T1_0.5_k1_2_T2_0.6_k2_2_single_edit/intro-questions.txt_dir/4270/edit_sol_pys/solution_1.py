

def main():
    num_of_ingredients = int(input())
    ingredients = list(map(float, input().split()))
    ingredients.sort(reverse=True)
    while len(ingredients) > 1: ingredients[0] = (ingredients[0] + ingredients[1]) / 2; ingredients.pop(1); ingredients.sort(reverse=True)
    print(ingredients[0])  

if __name__ == '__main__':
    main()
