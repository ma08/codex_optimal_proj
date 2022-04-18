
def main():
    N, B, H, W = map(int, input().split())
    minCost = 100000000
    for _ in range(H):
        cost = int(input())
        num_beds = list(map(int, input().split()))
        for i in range(len(num_beds)):
            if num_beds[i] >= N and cost*N <= B:
                minCost = min(minCost, cost*N)
    if minCost != 100000000:
        print(minCost)
    else:
        print("stay home")

main()
