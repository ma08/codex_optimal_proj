
import sys

def main():
    n, X = map(int, sys.stdin.readline().split())
    prices = list(map(int, sys.stdin.readline().split()))

    prices.sort()

    if prices[-1] + prices[-2] <= X:
        print(n)
        return

    if prices[0] + prices[1] > X:
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
