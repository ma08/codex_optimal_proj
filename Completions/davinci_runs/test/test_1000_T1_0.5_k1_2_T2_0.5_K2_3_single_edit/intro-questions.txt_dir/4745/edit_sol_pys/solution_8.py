

import sys

def main():
    n, X = list(map(int, sys.stdin.readline().split())) # n: length of array, X: max sum
    prices = list(map(int, sys.stdin.readline().split())) # prices: array of numbers

    prices.sort()

    if prices[-1] + prices[-2] <= X: # if the max two numbers are less than or equal to X, then all numbers are valid, so print length of array
        print(n) 
        return 

    if prices[0] + prices[1] > X: # if the min two numbers are greater than X, then no numbers are valid, so print 0
        print(0) 
        return 

    left = 0
    right = n-1

    while left < right:
        if prices[left] + prices[right] > X:
            right -= 1
        else:
            left += 1

    print(n - (right + 1))

if __name__ == '__main__':
    main()
