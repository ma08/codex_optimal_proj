

def main():
    N, B, H, W = map(int, input().split())  # N is the number of people, B is the budget, H is the number of hotels, W is the number of weeks
    min_price = B
    while H:
        H -= 1
        p = int(input())  # p is the price per person per night
        if p * N > B:
            continue
        a = list(map(int, input().split()))  # a is the list of available beds per week
        for b in a:
            if b >= N:
                min_price = min(min_price, p * N)
    if min_price == B:
        print("stay home")
    else:
        print(min_price)

main()
