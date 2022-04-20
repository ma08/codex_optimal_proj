


def is_multiple_of_9(n):
    if n % 9 == 0:
        return True
    else:
        return False


def main():
    n = int(input())
    if is_multiple_of_9(n):
        print("Yes")
    else:
        print("No")


if __name__ == '__main__':
    main()