


def main():
    n = int(input().strip())
    print(min_swap(n))


def min_swap(n):
    if n % 25 == 0:
        return 0
    n_str = str(n)
    if len(n_str) == 1:
        return -1
    if n_str[-2:] == '00':
        return -1

    for index in range(len(n_str) - 1, 0, -1):
        if n_str[index] != '0' and n_str[index - 1] != '0':
            return 1 + min_swap(n_str[:index - 1] + n_str[index] + n_str[index - 1] + n_str[index + 1:])

    return -1


if __name__ == '__main__':
    main()