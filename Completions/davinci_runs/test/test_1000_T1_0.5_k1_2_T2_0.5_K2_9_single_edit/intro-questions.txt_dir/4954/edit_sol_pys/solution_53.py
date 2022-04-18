

import sys

def main():
    N, B, H, W = [int(x) for x in sys.stdin.readline().split()]
    minCost = B + 1
    while True:
        price = int(sys.stdin.readline())
        beds = [int(x) for x in sys.stdin.readline().split()]  # number of beds
        for j in range(W):  # number of hotels
            if beds[j] >= N:  # if we have N beds
                cost = price * N  # total cost
                if cost < minCost:  # if cost is less than minCost
                    minCost = cost  # set minCost to cost
    if minCost <= B:  # if minCost is less than budget
        print(minCost)  # print minCost
    else:  # otherwise
        print("stay home")  # print stay home


main()
