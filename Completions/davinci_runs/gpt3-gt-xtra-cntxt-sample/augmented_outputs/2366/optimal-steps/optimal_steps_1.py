def get_num_bad_prices(array):
    array.sort()
    num_bad_prices = 0
    min_price = array[0]
    for price in array:
        if price < min_price:
            num_bad_prices += 1
        min_price = min(min_price, price)
    return num_bad_prices

def main():
    num_test_cases = int(input())
    for _ in range(num_test_cases):
        num_days = int(input())
        prices = [int(x) for x in input().split()]
        print(get_num_bad_prices(prices))

if __name__ == "__main__":
    main()