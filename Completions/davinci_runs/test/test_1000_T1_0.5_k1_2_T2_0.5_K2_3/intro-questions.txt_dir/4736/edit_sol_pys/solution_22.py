

def count_ascending_combos(numbers, K):
    if K == 0:
        return 1
    elif sum(numbers) < K:
        return 0
    else:
        ways = count_ascending_combos([n - 1 for n in numbers], K - 1)
        ways += sum([count_ascending_combos([n - 1 for n in numbers], K - 1 - i) for i in range(numbers[0])])
        return ways

def main():
    import sys
    numbers = [int(n) for n in sys.stdin.readline().split()]
    K = int(sys.stdin.readline())
    print(count_ascending_combos(numbers, K))

if __name__ == '__main__':
    main()
