

def main():
    num_ingredients = int(input())
    ingredient_list = list(map(int, input().split()))
    ingredient_list.sort()

    while len(ingredient_list) > 1:
        ingredient_list[0] = (ingredient_list[0] + ingredient_list[1]) / 2
        ingredient_list.pop(1)
        ingredient_list.sort()

    print(ingredient_list[0])

if __name__ == '__main__':
    main()
