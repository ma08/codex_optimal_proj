

def main():
    # get input
    n, b, h, w = map(int, input().split(" "))
    hotels = []
    for i in range(h):
        price = int(input())
        beds_available = list(map(int, input().split(" ")))
        hotels.append((price, beds_available))

    # calculate minimum cost
    min_cost = b + 1
    for hotel in hotels:
        price, beds_available = hotel
        if price * n >= b:
            continue
        for bed in beds_available:
            if bed >= n:
                min_cost = min(min_cost, price * n)
                break

    # print output
    if min_cost > b:
        print("stay home")
    else:
        print(min_cost)

if __name__ == "__main__":
    main()
