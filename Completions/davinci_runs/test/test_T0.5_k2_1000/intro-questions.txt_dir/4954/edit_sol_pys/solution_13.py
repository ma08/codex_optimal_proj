

def main():
    N, B, h, w = map(int, input().split())
    min_price = B + 1
    while h:
        h -= 1
        p = int(input())
        a = list(map(int, input().split()))
        for b in a:
            if b >= N:
                min_price = min(min_price, p * N)
    if min_price > B:
        print("stay home")
    else:
        print(min_price)

main()
