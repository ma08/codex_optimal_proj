

def main():
    n, m = map(int, input().rstrip().split())
    foods = [0] * (m+1)
    for i in range(1, n+1):
        k = int(input().rstrip().split()[0])
        for j in map(int, input().rstrip().split()[:k]):
            foods[j] += 1
    print(foods.count(n) - 1)

if __name__ == '__main__':
    main()
