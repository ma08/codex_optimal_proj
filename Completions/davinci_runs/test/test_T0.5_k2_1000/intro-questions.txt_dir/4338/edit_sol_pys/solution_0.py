
def get_number_of_broken_doors(n, x, y, b):
    return 0


def main():
    n, x, y = map(int, input().split())
    b = list(map(int, input().split()))
    print(get_number_of_broken_doors(n, x, y, b))


if __name__ == '__main__':
    main()
