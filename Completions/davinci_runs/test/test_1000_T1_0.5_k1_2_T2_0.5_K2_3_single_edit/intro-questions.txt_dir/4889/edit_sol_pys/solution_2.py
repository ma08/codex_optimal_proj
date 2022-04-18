

def main():
    # read in the number of test cases
    num_test_cases = int(input())

    # read in the test cases
    test_cases = [int(input()) for _ in range(num_test_cases)]

    # compute the number of coins needed for each test case
    coin_counts = []
    for test_case in test_cases:
        coin_counts.append(compute_coin_count(test_case))

    # print the number of coins needed for each test case
    for coin_count in coin_counts:
        print(coin_count)


def compute_coin_count(change):
    # initialize the number of coins
    num_coins = 0

    # compute the number of quarters
    num_coins += change // 25
    change %= 25

    # compute the number of dimes
    num_coins += change // 10
    change %= 10

    # compute the number of nickels
    num_coins += change // 5
    change %= 5

    # compute the number of pennies
    num_coins += change // 1

    # return the number of coins
    return num_coins

if __name__ == '__main__':
    main()
