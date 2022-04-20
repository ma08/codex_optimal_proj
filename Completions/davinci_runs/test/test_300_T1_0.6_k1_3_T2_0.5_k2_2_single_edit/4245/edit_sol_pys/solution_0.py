

def main():
    # get input from user
    a, b = map(int, input().split())

    # calculate power strips required
    power_strips = b // a
    if b % a:
        power_strips += 1

    # output result
    print(power_strips)


if __name__ == "__main__":
    main()
