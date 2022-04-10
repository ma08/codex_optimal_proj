

def main():
    """
    This is the main function.

    This function takes a number and a number of digits to get the remainder of
    and returns the minimum number of operations to make the remainder of the
    number the same as the remainder of the number of digits.

    This function uses the following local variables:

    n - number of digits in the number.
    x - the first number for the remainder.
    y - the second number for the remainder.
    number - the number to get the remainder of.
    remainder - the remainder of the number.
    answer - the minimum number of operations required.
    """
    n, x, y = [int(x) for x in input().split()]
    number = input()
    remainder = int(number[n - x:])
    answer = 0

    while remainder != int(str(10 ** x).ljust(y, '0')):
        remainder = (remainder - 1) % 10 ** x
        answer += 1

    return answer


if __name__ == "__main__":
    print(main())
