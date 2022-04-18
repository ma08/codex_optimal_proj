

import sys

def main():
    N,B,H,W = [int(x) for x in sys.stdin.readline().split()]
    minCost = B+1
    for i in range(H):
        price = int(sys.stdin.readline())
        beds = [int(x) for x in sys.stdin.readline().split()]
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