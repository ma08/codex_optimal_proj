
import sys

sys.setrecursionlimit(10**6)

def get_min_coins(amount, coins):
    if amount == 0:
        return 0, []
    if amount < 0:
        return None, None

    min_coins = sys.maxsize
    min_coins_list = None
    for c in coins:
        coins_count, coins_list = get_min_coins(amount - c, coins)
        if coins_count is not None and coins_count < min_coins:
            min_coins = coins_count
            min_coins_list = coins_list
    if min_coins == sys.maxsize:
        return None, None
    return min_coins + 1, coins_list + [c]

def main():
    T = int(sys.stdin.readline().strip())
    for t in range(T):
        amount = int(sys.stdin.readline().strip())
        coins = [1, 2, 5, 10, 20, 50, 100, 200, 500, 2000]
        coins_count, coins_list = get_min_coins(amount, coins)
        print(coins_count)
        print(" ".join(map(str, coins_list)))

if __name__ == "__main__":
    main()
