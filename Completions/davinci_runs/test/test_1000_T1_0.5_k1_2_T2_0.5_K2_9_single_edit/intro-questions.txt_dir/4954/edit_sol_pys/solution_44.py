

def main():
    # get input
    n, budget, h, w = map(int, input().split())
    hotels = []
    for i in range(h):
        price = int(input())
        beds = list(map(int, input().split()))
        hotels.append((price, beds))

    # calculate minimum cost
    min_cost = budget + 1
    for hotel in hotels:
        price, beds = hotel
        if price * n > budget:
            continue
        for bed in beds:
            if bed >= n:
                min_cost = min(min_cost, price * n)
                break

    # print output
    if min_cost > budget:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
