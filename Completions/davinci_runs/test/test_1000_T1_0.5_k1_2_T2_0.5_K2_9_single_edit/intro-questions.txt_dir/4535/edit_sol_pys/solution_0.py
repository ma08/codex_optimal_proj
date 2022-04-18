

def hammingWeight(n):
    n = n & 0xffffffff
    count = 0
    while n > 0:
        n &= n - 1
        count += 1
    return count


def hammingWeight_bit_operation(n):
    n = n & 0xffffffff
    count = 0
    while n > 0:
        if n & 1 == 1:
            count += 1
        n >>= 1
    return count


def hammingWeight_bin(n):
    return bin(n & 0xffffffff).count("1")


if __name__ == '__main__':
    print(hammingWeight(11))
    print(hammingWeight_bit_operation(11))
    print(hammingWeight_bin(11))
