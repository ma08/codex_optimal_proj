
def reverse_bin(n):
    return int(bin(n)[2:][::-1], 2)


if __name__ == '__main__':
    print(reverse_bin(int(input())))
