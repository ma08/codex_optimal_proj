import sys

def main():
    juices = list(map(int, sys.stdin.readline().split()))
    recipe = list(map(int, sys.stdin.readline().split()))
    min_cocktail = min(juices[0] // recipe[0], juices[1] // recipe[1], juices[2] // recipe[2])
    for j in range(0, 3):
        print(juices[j] - min_cocktail * recipe[j], end=' ')

main()
