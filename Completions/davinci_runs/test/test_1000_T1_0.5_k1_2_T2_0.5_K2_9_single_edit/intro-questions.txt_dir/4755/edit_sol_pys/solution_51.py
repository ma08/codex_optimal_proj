

def round(c, k):
    return c - c % 10 ** k + 10 ** k if c % 10 ** k >= 5 * 10 ** (k - 1) else c - c % 10 ** k


def main():
    c, k = map(int, input().split())
    print(round(c, k))


if __name__ == '__main__':
    main()
