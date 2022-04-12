

def main():
    # get inputs
    n, b, h, w = map(int, input().split()) # n = number of people, b = budget, h = number of hotels, w = number of weeks
    hotels = []
    for i in range(h):
        price = int(input()) # price per person per week
        beds = list(map(int, input().split()))
        hotels.append((price, beds)) # hotels = [(price, [beds]), ...]

    # calculate minimum cost
    min_cost = b + 1 # if no hotel is found, min_cost will be greater than b
    for hotel in hotels:
        price, beds = hotel
        if price * n > b: # if the price per person per week times the number of people is greater than the budget, skip this hotel
            continue
        for bed in beds:
            if bed >= n: # if the number of beds is greater than or equal to the number of people, update the minimum cost
                min_cost = min(min_cost, price * n)
                break

    # print outputs
    if min_cost > b: # if the minimum cost is greater than the budget, print "stay home"
        print("stay home")
    else: # otherwise, print the minimum cost
        print(min_cost)

if __name__ == "__main__":
    main()
