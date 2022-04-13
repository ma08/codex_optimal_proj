
def reverse_bin(n):
    return int(bin(int(n, 2))[2:][::-1], 2)


if __name__ == '__main__':
    print(reverse_bin(input()))
