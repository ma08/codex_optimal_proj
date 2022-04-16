

def main():
    N, B, H, W = map(int, input().split())
    min_price = B
    while H:
        H -= 1
        p = int(input())
        if p * N > B:
            continue
        beds = list(map(int, input().split()))
        for bed in beds:
            if bed >= N:
                min_price = min(min_price, p * N)
    if min_price == B:
        print("stay home")
    else:
        print(min_price)

main()
