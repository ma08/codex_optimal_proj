

def main():
    # X = input()
    # X = int(X)
    X = 1024

    coins = [500, 100, 50, 10, 5, 1]
    points = [1000, 0, 0, 0, 5, 0]
    num_coins = [0, 0, 0, 0, 0, 0]

    for i in range(len(coins)):
        num_coins[i] = X // coins[i]
        X -= num_coins[i] * coins[i]
        points[i] *= num_coins[i]
        print("{}-yen coin: {}".format(coins[i], num_coins[i]))
        print("Happiness points: {}".format(points[i]))

    print("Total happiness points: {}".format(sum(points)))

if __name__ == '__main__':
    main()