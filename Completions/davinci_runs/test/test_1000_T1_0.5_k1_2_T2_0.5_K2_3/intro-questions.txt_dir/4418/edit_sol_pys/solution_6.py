


def find_index(a: list, x: int, start: int=0):
    for i in range(start, len(a)):
        if a[i] == x:
            return i
    return -1


def delete_numbers(a: list):
    while True:
        if len(a) == 0:
            return 0
        if len(a) % 6 != 0:
            return len(a)
        if a[0] == 4:
            i = 0
            for x in [8, 15, 16, 23, 42]:
                i = find_index(a, x, i + 1)
                if i == -1:
                    return len(a)
        else:
            return len(a)
        a = a[i + 1:]



def main():
    n = int(input())
    a = list(map(int, input().split()))
    print(delete_numbers(a))


if __name__ == '__main__':
    main()
