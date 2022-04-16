

def get_number_of_broken_doors(n, x, y, a, b):
    return 0


def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    print(get_number_of_broken_doors(n, x, y, a, b))


if __name__ == '__main__':
    main()
