
from collections import defaultdict

def main():
    n, m = map(int, input().split())
    foods = defaultdict(int)
    for i in range(n):
        k = int(input().split()[0])
        for j in map(int, input().split()):
            foods[j] += 1
    print(sum(1 for f in foods.values() if f == n))

if __name__ == '__main__':
    main()
