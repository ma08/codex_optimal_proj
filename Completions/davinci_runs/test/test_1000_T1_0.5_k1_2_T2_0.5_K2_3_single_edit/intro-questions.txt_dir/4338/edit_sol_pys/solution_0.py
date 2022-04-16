

def get_number_of_broken_doors(n, x, y, a):
    return n


def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))  # noqa: F821
    print(get_number_of_broken_doors(n, x, y, a))


if __name__ == '__main__':
    main()
