

def main():
    N, B, H, W = map(int, input().split())
    minCost = 1000000
    for _ in range(H):
        cost = int(input())
        numBeds = list(map(int, input().split()))
        for i in range(len(numBeds)):
            if numBeds[i] >= N and cost*N <= B:
                minCost = min(minCost, cost*N)
    if minCost != 1000000:
        print(minCost)
    else:
        print("stay home") 

main()
