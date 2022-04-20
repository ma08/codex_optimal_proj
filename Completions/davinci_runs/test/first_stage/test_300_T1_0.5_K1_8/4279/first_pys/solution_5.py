

def main():
    q = int(input())
    for i in range(q):
        k = int(input())
        print(get_digit(k))

def get_digit(k):
    if k == 1:
        return 1
    block_size = 1
    cur_block_start = 1
    while cur_block_start + block_size < k:
        cur_block_start += block_size
        block_size += 1
    return str(block_size)[k - cur_block_start - 1]

if __name__ == "__main__":
    main()