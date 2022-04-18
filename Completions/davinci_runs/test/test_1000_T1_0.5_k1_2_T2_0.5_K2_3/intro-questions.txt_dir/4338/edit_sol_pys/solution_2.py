

def get_number_of_broken_doors(n, x, y, doors, doors_broken):
    return n


def main():
    n, x, y = map(int, input().split())
    doors = list(map(int, input().split()))
    doors_broken = [0] * n
    print(get_number_of_broken_doors(n, x, y, doors, doors_broken))


if __name__ == '__main__':
    main()
