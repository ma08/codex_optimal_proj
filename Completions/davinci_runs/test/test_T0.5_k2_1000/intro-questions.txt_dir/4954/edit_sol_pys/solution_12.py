

def main():
    # get the input
    n, b, h, w = map(int, raw_input().split())
    hotels = []
    for i in range(h):
        price = int(raw_input())
        beds = list(map(int, raw_input().split()))
        hotels.append((price, beds))

    # calculate the minimum cost
    min_cost = b + 1
    for hotel in hotels:
        price, beds = hotel
        if price * n > b:
            continue
        for bed in beds:
            if bed >= n:
                min_cost = min(min_cost, price * n)
                break

    # print the output
    if min_cost > b:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
