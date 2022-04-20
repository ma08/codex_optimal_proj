

def main():
    n, m = map(int, input().split())
    a = list(map(int, input().split()))
    offers = []
    for _ in range(m):
        offers.append(list(map(int, input().split())))

    # find the minimum cost of connecting 1 to any other node
    min_cost = a[0]
    for offer in offers:
        if offer[0] == 1:
            if offer[2] < a[offer[1] - 1]:
                min_cost += offer[2]
            else:
                min_cost += a[offer[1] - 1]

    # find the minimum cost of connecting any other node to 1
    for i in range(2, n):
        min_cost_i = a[i - 1]
        for offer in offers:
            if offer[1] == i:
                if offer[2] < a[offer[0] - 1]:
                    min_cost_i += offer[2]
                else:
                    min_cost_i += a[offer[0] - 1]
        min_cost = min(min_cost, min_cost_i)

    print(min_cost)


if __name__ == '__main__':
    main()
