

def get_factors(number):
    factors = []
    for i in range(1, number + 1):
        if number % i == 0:
            factors.append(i)
    return factors


def is_perfect_number(number):
    return sum(get_factors(number)) == 2 * number


def get_perfect_numbers(n):
    perfect_numbers = []
    for i in range(1, n + 1):
        if is_perfect_number(i):
            perfect_numbers.append(i)
    return perfect_numbers


if __name__ == "__main__":
    user_input = int(input("Enter n: "))
    print("Perfect numbers:", get_perfect_numbers(user_input))
