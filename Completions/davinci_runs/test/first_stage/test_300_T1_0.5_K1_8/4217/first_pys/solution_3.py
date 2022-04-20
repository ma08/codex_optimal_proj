

def main():
    n, m = map(int, input().split())
    foods = [0 for i in range(m)]

    for i in range(n):
        k = int(input().split()[0])
        for j in range(k):
            foods[int(input().split()[0]) - 1] += 1

    print(foods.count(n))

if __name__ == '__main__':
    main()