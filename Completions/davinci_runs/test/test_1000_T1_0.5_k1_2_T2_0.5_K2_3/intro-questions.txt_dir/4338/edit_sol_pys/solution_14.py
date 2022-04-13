

def get_number_of_broken_doors(n, x, y, a, b):
    return n


def main():
    n, x, y = map(int, input().split())
    a = list(map(int, input().split()))  # a is the list of door numbers
    b = list(map(int, input().split()))  # b is the list of door states
    print(get_number_of_broken_doors(n, x, y, a, b))


if __name__ == '__main__':
    main()
