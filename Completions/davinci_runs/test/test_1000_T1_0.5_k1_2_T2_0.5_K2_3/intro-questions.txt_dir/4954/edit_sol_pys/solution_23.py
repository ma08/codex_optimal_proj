

def main():
    N, B, H, W = map(int, input().split()) # N: # of guests, B: budget, H: # of hotels, W: # of weeks
    minCost = 100000000
    for _ in range(H):
        cost = int(input())
        numBeds = list(map(int, input().split())) # number of beds each week
        for i in range(len(numBeds)):
            if numBeds[i] >= N and cost*N <= B:
                minCost = min(minCost, cost*N)
    if minCost != 100000000:
        print(minCost)
    else:
        print("stay home") 

main()
