

def main():
    N, B, H, W = map(int, input().split())
    min_price = B
    for _ in range(H):
        p = int(input())
        if p * N > B:
            continue
        a = list(map(int, input().split()))
        if max(a) >= N:
            min_price = min(min_price, p * N)
    if min_price == B:
        print("stay home")
    else:
        print(min_price)

main()
