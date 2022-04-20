


def main():
    # get input
    a, b = map(int, input().split())

    # calculate power strips required
    power_strips = (b + a - 1) // a

    # output result
    print(power_strips)


if __name__ == "__main__":
    main()
