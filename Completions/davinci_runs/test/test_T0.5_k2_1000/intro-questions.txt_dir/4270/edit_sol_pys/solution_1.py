
def main():
    _ = int(input())
    ingredient = list(map(int, input().split()))
    ingredient.sort()

    while len(ingredient) > 1:
        ingredient[0] = (ingredient[0] + ingredient[1]) / 2.0
        ingredient.pop(1)
        ingredient.sort()

    print(ingredient[0])

if __name__ == '__main__':
    main()
