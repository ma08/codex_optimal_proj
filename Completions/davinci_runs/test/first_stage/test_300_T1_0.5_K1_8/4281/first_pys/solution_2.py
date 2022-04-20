

def main():
    n = int(input())
    x = list(map(int, input().split()))

    min_houses = max_houses = 1
    count = 1
    for i, j in zip(x, x[1:]):
        if i == j:
            count += 1
        else:
            min_houses += 1
            max_houses += count
            count = 1
    max_houses += count

    print(min_houses, max_houses)


main()