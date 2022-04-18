

import sys

def main():
    input_ = sys.stdin.read().splitlines()
    prices = input_[0].split()
    a, b = int(prices[0]), int(prices[1])
    maxes = input_[1].split()
    m, sigma = int(maxes[0]), int(maxes[1])
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
