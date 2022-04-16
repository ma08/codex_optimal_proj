

import sys

def main():
    input = sys.stdin.read().splitlines()
    prices = [int(i) for i in input[0].split()]
    a = prices[0]
    b = prices[1]
    maxes = [int(i) for i in input[1].split()]
    m = maxes[0]
    sigma = maxes[1]
    maxRent = 0
    for x in range(1, m//2+1):
        y = m - x
        if y < 1:
            break
        if 2*x + y >= sigma:
            rent = a*x + b*y
            if rent > maxRent:
                maxRent = rent
    print(maxRent)

main()
