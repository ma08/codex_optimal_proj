import math


def main():
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(get_digit(k))

def get_digit(k):
    if k == 1:
        return 1
    else:
        block_num = get_block_num(k) - 1
        block_start = get_block_start(block_num) - 1
        block_end = get_block_end(block_num) - 1
        block_length = block_end - block_start
        block_offset = k - block_start - 1
        digit = block_offset % (block_length + 1)
        return digit + 1

def get_block_num(k):
    return int(math.ceil(math.sqrt(2 * k + 0.25) - 0.5))

def get_block_start(block_num):
    return (block_num - 1) * block_num // 2 + 1 + 1

def get_block_end(block_num):
    return block_num * (block_num + 1) // 2 + 1

if __name__ == '__main__':
    main()
