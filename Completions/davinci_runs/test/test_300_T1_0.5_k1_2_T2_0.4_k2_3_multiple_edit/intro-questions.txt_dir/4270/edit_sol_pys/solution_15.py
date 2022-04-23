

def main():
    #num_ingredient = int(input())
    ingredient = list(map(int, input().split()))
    ingredient.sort(reverse=True)

    while len(ingredient) > 1:
        ingredient[0] = (ingredient[0] + ingredient[1]) / 2
        ingredient.pop(1)
        ingredient.sort(reverse=True)

    print(ingredient[0])

if __name__ == '__main__':
    main()
