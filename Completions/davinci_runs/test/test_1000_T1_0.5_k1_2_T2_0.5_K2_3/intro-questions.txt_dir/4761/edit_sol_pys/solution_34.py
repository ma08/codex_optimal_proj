


def main():
    """ Main function.
    """
    l, h = [int(x) for x in input().split()]  # noqa: WPS221
    count = 0
    for i in range(l, h + 1):  # noqa: WPS221
        if is_valid(str(i)):  # noqa: WPS221

            count += 1

    print(count)

def is_valid(c):
    """ Check if the given number is valid.
    """
    if len(c) != 6 or any([x == '0' for x in c]):
        return False
    if len(set(c)) != 6:  # noqa: WPS221
        return False
    for i in c:
        if int(c) % int(i) != 0:
            return False
    return True


if __name__ == '__main__':
    main()
