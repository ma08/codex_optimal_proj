
from collections import Counter

def main():
    n, m = map(int, input().split())
    foods = Counter()
    for i in range(n):
        k = int(input().split()[0])
        for j in map(int, input().split()):
            foods[j] += 1
    print(foods.values().count(n))

if __name__ == '__main__':
    main()
