

def count_ascending_combos(numbers, K):
    # Base case: if there are no more cards left to deal, return 1
    if K == 0:
        return 1
    # Base case: if there are more cards to deal than there are cards in the deck, return 0
    elif sum(numbers) < K or sum(numbers) == 0:
        return 0
    else:
        # Initialize with the number of ways to deal a strictly ascending sequence without the first card
        ways = count_ascending_combos([n - 1 for n in numbers], K - 1)
        # Add the number of ways to deal a strictly ascending sequence with the first card
        ways += sum([count_ascending_combos([n - 1 for n in numbers], K - 1 - i) for i in range(numbers[0])])
        return ways

def main():
    import sys
    numbers = [int(n) for n in sys.stdin.readline().split()]
    K = int(sys.stdin.readline())
    print(count_ascending_combos(numbers, K))

if __name__ == '__main__':
    main()
