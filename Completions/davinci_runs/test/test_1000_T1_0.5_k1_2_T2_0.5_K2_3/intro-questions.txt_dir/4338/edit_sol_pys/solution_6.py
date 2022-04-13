

def get_number_of_broken_doors(n, x, y, doors, start):
    return n


def main():
    n, x, y = map(int, input().split())
    doors = list(map(int, input().split()))
    start = input()
    print(get_number_of_broken_doors(n, x, y, doors, start))


if __name__ == '__main__':
    main()
