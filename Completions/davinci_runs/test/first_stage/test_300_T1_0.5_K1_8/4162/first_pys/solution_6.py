


def main():
    N = int(input())
    A = [int(n) for n in input().split()]

    # The maximum value of f is the sum of a_i - 1
    # because f(m) = sum(a_i - 1) when m = LCM(a_1, a_2, ..., a_N)
    print(sum(A) - N)


if __name__ == '__main__':
    main()