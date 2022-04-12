
import sys

def main():
    N,B,H,W = [int(x) for x in sys.stdin.readline().split()] # N: number of people, B: budget, H: number of hotels, W: number of weeks
    minCost = B+1
    for i in range(H):
        price = int(sys.stdin.readline())
        beds = [int(x) for x in sys.stdin.readline().split()] # number of available beds for each week
        for j in range(W):
            if beds[j] >= N:
                cost = price*N
                if cost < minCost:
                    minCost = cost
    if minCost <= B:
        print(minCost)
    else:
        print("stay home")

main()
