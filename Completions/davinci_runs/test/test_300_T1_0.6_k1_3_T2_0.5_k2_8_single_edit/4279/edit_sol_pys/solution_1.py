

def get_pos(k):
    """
    Returns the position of the digit at position k in the sequence
    """
    # Get the index of the block that k is in
    block_index = 0
    while 10**block_index < k:
        block_index += 1
    # Get the number of digits in the block that k is in
    block_size = block_index * 9 * 10**(block_index - 1)
    # Get the index of the number that k is in
    # This is the index of the number in the block that k is in
    num_index = (k - 1) // block_index
    # Get the number that k is in
    # This is the number in the block that k is in
    num = 10**(block_index - 1) + num_index
    # Get the index of the digit that k is in
    # This is the index of the digit in the number that k is in
    digit_index = (k - 1) % block_index
    # Get the position of the digit that k is in
    # This is the position of the digit in the number that k is in
    pos = int(str(num)[digit_index])
    return pos

q = int(input())
for i in range(q):
    k = int(input())
    print(get_pos(k))
