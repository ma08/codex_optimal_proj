


def main():
    n = int(input())
    divisors = list(map(int, input().split()))

    x_divisors = []
    y_divisors = []

    for divisor in divisors:
        if divisor in x_divisors:
            y_divisors.append(divisor)
        else:
            x_divisors.append(divisor)

    x = 1
    for divisor in x_divisors:
        x *= divisor

    y = 1
    for divisor in y_divisors:
        y *= divisor

    print(x, y)


if __name__ == "__main__":
    main()