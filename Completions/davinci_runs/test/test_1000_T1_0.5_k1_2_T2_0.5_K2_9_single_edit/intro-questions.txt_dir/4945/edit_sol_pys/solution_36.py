

import sys

def main():
    input = sys.stdin.read().splitlines()
    prices = input[0].split()
    a = int(prices[0])
    b = int(prices[1])
    maxes = input[1].split()
    m = int(maxes[0])
    sigma = int(maxes[1])
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
