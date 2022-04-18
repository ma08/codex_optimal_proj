from sys import stdin

def main():
    t = int(stdin.readline().strip())
    for i in range(t):
        n = int(stdin.readline().strip())
        prices = [int(x) for x in stdin.readline().strip().split()]
        stack = []
        bad_prices = 0
        for price in prices:
            while stack and stack[-1] > price:
                stack.pop()
            stack.append(price)
            bad_prices += len(stack) - 1
        print(bad_prices)

if __name__ == '__main__':
    main()