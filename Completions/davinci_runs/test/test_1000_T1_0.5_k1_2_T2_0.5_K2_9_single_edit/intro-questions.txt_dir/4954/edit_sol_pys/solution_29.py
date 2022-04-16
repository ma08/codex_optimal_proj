

def getMinCost(N, B, H, W):
    minCost = 100000000
    for _ in range(H):
        cost = int(input())
        numBeds = list(map(int, input().split()))
        for i in range(len(numBeds)):
            if numBeds[i] >= N and cost*N <= B:
                minCost = min(minCost, cost*N)
    if minCost != 100000000:
        return minCost
    else:
        return "stay home"

def main():
    N, B, H, W = map(int, input().split())
    print(getMinCost(N, B, H, W))

main()
