def find_bad_prices(prices):
    stack = []
    for i in range(len(prices)):
        while stack and prices[i] < prices[stack[-1]]:
            bad_price = stack.pop()
            print("Price at index " + str(bad_price) + " is bad")
        stack.append(i)
    return stack

prices = [3, 9, 4, 6, 7, 5]
find_bad_prices(prices)