import sys

def main():
    # Read the number of test cases
    t = int(sys.stdin.readline())
    # For each test case
    for i in range(t):
        # Read the number of days and the prices
        n = int(sys.stdin.readline())
        prices = list(map(int, sys.stdin.readline().split()))
        # Initialize the stack
        stack = []
        count = 0
        # For each price
        for price in prices:
            # While the stack is not empty and the top of the stack is lower
            while stack and stack[-1] > price:
                # Pop the stack
                stack.pop()
                # Increase the count
                count += 1
            # Push the price to the stack
            stack.append(price)
        # Print the count
        print(count)

if __name__ == '__main__':
    main()