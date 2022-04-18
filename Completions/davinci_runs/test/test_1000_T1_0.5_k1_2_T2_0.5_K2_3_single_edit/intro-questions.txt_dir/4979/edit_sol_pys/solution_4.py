
def reverse_binary(num):
    return int(str(bin(num))[:1:-1], 2)


def main():
    print(reverse_binary(int(input())))


if __name__ == '__main__':
    main()
