

def main():
    n = int(input())
    a = list(map(int, input().split()))[:n]
    # print(a)

    # find the minimum cost of connecting 1 to any other node
    min_cost = a[0] + a[1]
    for i in range(2, n):
        if a[i] < min_cost:
            min_cost = a[i]

    print(min_cost + a[0])


if __name__ == '__main__':
    main()
