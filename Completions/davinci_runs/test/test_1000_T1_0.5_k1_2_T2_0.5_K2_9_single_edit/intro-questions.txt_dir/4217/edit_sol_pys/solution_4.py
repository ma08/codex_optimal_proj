
def main():
    n, m = map(int, input().split())  # n: number of people, m: number of foods
    foods = [0] * m  # number of people who ate the food
    for i in range(n):  # count the number of people who ate the food
        k = int(input().split()[0])
        for j in map(int, input().split()):
            foods[j-1] += 1
    print(foods.count(n))

if __name__ == '__main__':
    main()
