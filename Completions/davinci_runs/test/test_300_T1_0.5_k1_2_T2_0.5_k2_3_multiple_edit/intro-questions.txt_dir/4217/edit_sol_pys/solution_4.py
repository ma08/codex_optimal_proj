

def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k = list(map(int, input().split()))
        for j in k[1:]:
            foods[j-1] += 1
    print(foods.count(n))

if __name__ == '__main__':
    main()
