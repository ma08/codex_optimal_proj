

def main():
    # read the input
    n = int(input())

    # check if the number is already divisible by 25
    if n % 25 == 0:
        print(0)
        return

    # convert the number to a string
    n_str = str(n)

    # count the number of leading zeroes
    n_zeroes = 0
    for i in range(0, len(n_str)):
        if n_str[i] == '0':
            n_zeroes += 1
        else:
            break

    # check if the number of leading zeroes is more than 1
    if n_zeroes > 1:
        print(-1)
        return

    # count the number of zeroes in the number
    n_zeroes = n_str.count('0')

    # check if the number of zeroes is more than 1
    if n_zeroes > 1:
        print(-1)
        return

    # count the number of 2s and 5s in the number
    n_twos = n_str.count('2')
    n_fives = n_str.count('5')

    # check if the number of 2s and 5s is more than 1
    if n_twos > 1 or n_fives > 1:
        print(-1)
        return

    # check if the number has a 2 and a 5
    if n_twos == 1 and n_fives == 1:
        print(1)
        return

    # check if the number has a 2 or a 5
    if n_twos == 1 or n_fives == 1:
        print(2)
        return

    # check if the number has a zero
    if n_zeroes == 1:
        print(3)
        return

    print(4)


if __name__ == "__main__":
    main()