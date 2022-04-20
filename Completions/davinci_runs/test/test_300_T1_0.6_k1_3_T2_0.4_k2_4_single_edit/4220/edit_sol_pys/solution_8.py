


def main():
    k, s = input(), input()
    if k > len(s):
        print(s)
    else:
        print(s[:k] + '...')


if __name__ == '__main__':
    main()
