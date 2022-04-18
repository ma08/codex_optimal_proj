



def find_max(a, b):
    if a < b:
        return b
    else:
        return a


def main():
    a, b = input().split()
    a = int(a)
    b = int(b)
    print(find_max(a, b))


if __name__ == '__main__':
    main()
