

#------------------------------------------------------------------------------#

# https://oeis.org/A007814
# https://oeis.org/A007814/b007814.txt

#------------------------------------------------------------------------------#

from math import log10

def digit_at_pos(n):
    if n == 0:
        return 0

    # the length of the first n blocks
    length_n_blocks = (n*(n+1))//2

    # the length of the nth block
    length_nth_block = n

    # the number of digits in the nth block
    num_digits_nth_block = int(log10(n)) + 1

    # the length of the first n-1 blocks
    length_n_minus_1_blocks = length_n_blocks - length_nth_block

    # the number of digits in the first n-1 blocks
    num_digits_n_minus_1_blocks = length_n_minus_1_blocks - (n-1)

    # the number of digits in the first n-1 blocks of the nth block
    num_digits_n_minus_1_blocks_nth_block = num_digits_n_minus_1_blocks - (num_digits_nth_block - 1)

    # the number of digits in the nth block
    num_digits_nth_block = num_digits_nth_block + num_digits_n_minus_1_blocks_nth_block

    # the number of digits in the n blocks
    num_digits_n_blocks = num_digits_n_minus_1_blocks + num_digits_nth_block

    # the number of digits in the n-1 blocks
    num_digits_n_minus_1_blocks = num_digits_n_minus_1_blocks + num_digits_nth_block - 1

    # the digit number of the digit we want
    digit_num = n - length_n_minus_1_blocks - 1

    # the number of the block that contains the digit we want
    block_num = n - digit_num//num_digits_nth_block - 1

    # the block that contains the digit we want
    block = str(block_num + 1)

    # the digit we want
    digit = block[digit_num%num_digits_nth_block]

    return int(digit)

#------------------------------------------------------------------------------#

q = int(input())

for _ in range(q):
    k = int(input())

    print(digit_at_pos(k-1))