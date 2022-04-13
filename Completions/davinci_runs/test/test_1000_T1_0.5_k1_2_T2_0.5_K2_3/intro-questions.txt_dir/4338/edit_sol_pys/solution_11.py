

def get_number_of_broken_doors(n, x, y, doors):
    count = 0
    for i in range(n):
        if doors[i] <= x:
            count += 1
        elif doors[i] > y:
            count += 2
    return count


def main():
    n, x, y = map(int, input().split())
    doors = list(map(int, input().split()))
    print(get_number_of_broken_doors(n, x, y, doors))


if __name__ == '__main__':
    main()
