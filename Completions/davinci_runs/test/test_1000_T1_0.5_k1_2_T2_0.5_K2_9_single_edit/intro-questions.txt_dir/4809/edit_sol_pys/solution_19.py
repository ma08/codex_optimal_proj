

def coconut_splat(s, n):
    return (n - 1) % s + 1


def main():
    s, n = map(int, input().split())
    print(coconut_splat(s, n))


if __name__ == '__main__':
    main()
