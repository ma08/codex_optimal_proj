

def main():
    N, B, H, W = map(int, input().split())
    minCost = 100000000
    for _ in range(H):
        cost = int(input())
        numBeds = list(map(int, input().split()))
        for numBed in numBeds:
            if numBed >= N and cost*N <= B:
                minCost = min(minCost, cost*N)
    if minCost != 100000000:
        print(minCost)
    else:
        print("stay home")

main()
