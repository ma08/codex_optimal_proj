from collections import Counter

def main():
    n, m = map(int, input().split())
    foods = Counter()
    for i in range(n):
        k = int(input().split()[0])
        for j in map(int, input().split()):
            foods[j] += 1
    print(len([k for k, v in foods.items() if v == n]))

if __name__ == '__main__':
    main()
