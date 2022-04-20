


def get_divisors(x):
    divisors = []
    for i in range(1, x + 1):
        if x % i == 0:
            divisors.append(i)
    return divisors


def get_x_y(divisors):
    divisors_set = set(divisors)
    divisors_set.remove(1)
    for i in divisors_set:
        if divisors.count(i) == 1:
            return i, i
    return 1, 1


def main():
    n = int(input())
    divisors = list(map(int, input().split()))
    x, y = get_x_y(divisors)
    print(x, y)


if __name__ == "__main__":
    main()