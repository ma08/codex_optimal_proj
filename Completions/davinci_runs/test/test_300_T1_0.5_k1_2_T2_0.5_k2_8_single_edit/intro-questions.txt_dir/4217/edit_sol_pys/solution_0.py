

def main():
    n, m = map(int, input().split())
    foods = [0] * m
    for i in range(n):
        k = int(input().split()[0])
        for j in map(int, input().split()):
            foods[j-1] += 1
    print(foods.count(n)) # count the number of elements that are equal to n

if __name__ == '__main__':
    main()
