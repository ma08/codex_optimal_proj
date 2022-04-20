

import math

def main():
    q = int(input())
    for _ in range(q):
        k = int(input())
        print(get_digit(k))

def get_digit(k):
    if k == 1:
        return 1
    start = 1
    end = 1
    while end < k:
        start = end + 1
        end = end + 9*10**(int(math.log10(end)) + 1)*(int(math.log10(end)) + 1)
    start_block = start
    end_block = end
    block_number = int(math.log10(start_block)) + 1
    while start_block < k:
        k -= start_block
        start_block += block_number
    number = int(math.floor(start_block / block_number))
    return int(str(number)[k-1])

main()