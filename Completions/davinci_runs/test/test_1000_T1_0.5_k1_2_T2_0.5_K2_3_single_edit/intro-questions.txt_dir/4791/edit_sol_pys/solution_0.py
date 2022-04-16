def max_product(numbers):
    numbers.sort()
    return max(numbers[0] * numbers[1], numbers[2] * numbers[3])


def main():
    numbers = list(map(int, input().split()))
    print(max_product(numbers))


if __name__ == "__main__":
    main()
