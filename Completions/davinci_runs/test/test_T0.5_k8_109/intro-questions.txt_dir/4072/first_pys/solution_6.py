


def is_lucky(number):
    first_half = 0
    second_half = 0

    while number > 0:
        first_half += number % 10
        number //= 10
        second_half += number % 10
        number //= 10

    return first_half == second_half


def main():
    number = int(input())
    print(int(is_lucky(number)))


if __name__ == '__main__':
    main()