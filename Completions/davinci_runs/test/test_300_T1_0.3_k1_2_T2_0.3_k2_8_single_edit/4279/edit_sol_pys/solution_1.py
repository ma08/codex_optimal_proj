import math


def main():
    t = int(input())
    for _ in range(t):
        n = int(input())
        print(get_digit(n))

def get_digit(n):
    if n == 1:
        return 1
    else:
        block_num = get_block_num(n)
        block_start = get_block_start(block_num)
        block_end = get_block_end(block_num)
        block_length = block_end - block_start + 1
        block_offset = n - block_start
        digit = block_offset % block_length
        return digit + 1

def get_block_num(k):
    return int(math.ceil(math.sqrt(2 * k)))

def get_block_start(block_num):
    return (block_num - 1) * block_num // 2 + 1

def get_block_end(block_num):
    return block_num * (block_num + 1) // 2

if __name__ == '__main__':
    main()
