

def get_digit(k, n):
    """
    Returns the digit at position k in the sequence
    """
    if k == 0:
        return 0
    # Get the number of digits in the number that k corresponds to
    # This is the number of digits in the block that k is in
    num_digits = 1
    while n**num_digits < k:
        num_digits += 1
    # Get the index of the number that k corresponds to
    # This is the index of the number in the block that k is in
    num_index = (k - n**(num_digits - 1)) // num_digits
    # Get the number that k corresponds to
    # This is the number in the block that k is in
    num = n**(num_digits - 1) + num_index
    # Get the index of the digit that k corresponds to
    # This is the index of the digit in the number that k is in
    digit_index = (k - n**(num_digits - 1)) % num_digits
    # Get the digit that k corresponds to
    # This is the digit in the number that k is in
    digit = int(str(num)[digit_index])
    return digit

q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    print(get_digit(k - 1, n))
