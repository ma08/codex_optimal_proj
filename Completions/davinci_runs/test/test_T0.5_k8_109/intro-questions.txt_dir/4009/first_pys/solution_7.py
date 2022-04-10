

def main():
    n, x, y = map(int, input().split())
    num = list(map(int, input()))

    # find the first digit that is not 1
    i = 0
    while num[i] == 1:
        i += 1

    # now i is the first digit that is not 1
    # we need to change i+y digits to make the number % 10^x == 10^y
    # the first digit that is not changed is the (i+y)-th digit
    # so we need to change i+y-1 digits
    # we can change the first digit to 0 and change the rest of the digits to 1
    # so we need to change i+y-1-i = y-1 digits
    # if y-1 < 0, then the number is already satisfy the condition
    if y-1 < 0:
        print(0)
    else:
        print(y-1)


if __name__ == '__main__':
    main()