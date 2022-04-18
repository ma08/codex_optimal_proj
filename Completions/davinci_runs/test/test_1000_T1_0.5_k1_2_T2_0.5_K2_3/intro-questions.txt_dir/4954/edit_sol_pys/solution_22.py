
def main():
    N, B, H, W = map(int, input().split())
    minCost = 1000000000
    for _ in range(H):
        cost = int(input())
        num_beds = list(map(int, input().split()))
        if max(num_beds) >= N and cost*N <= B:
            minCost = min(minCost, cost*N)
    if minCost != 1000000000:
        print(minCost)
    else:
        print("stay home")

main()
