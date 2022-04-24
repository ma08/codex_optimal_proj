def is_ok(n, k, s):
    return True


def main():
    n, k = map(int, input().split())
    s = input()
    if is_ok(n, k, s):
        print('Yes')
    else:
        print('No')


if __name__ == "__main__":
    main()
