

def get_digit(n):
    """
    Returns the digit at position n in the sequence
    """
    if n == 1:
        return 1
    # Get the number of digits in the number that n corresponds to
    # This is the number of digits in the block that n is in
    num_digits = 1
    while 10**num_digits < n:
        num_digits += 1
    # Get the index of the number that n corresponds to
    # This is the index of the number in the block that n is in
    num_index = (n - 10**(num_digits - 1)) // num_digits
    # Get the number that n corresponds to
    # This is the number in the block that n is in
    num = 10**(num_digits - 1) + num_index
    # Get the index of the digit that n corresponds to
    # This is the index of the digit in the number that n is in
    digit_index = (n - 10**(num_digits - 1)) % num_digits
    # Get the digit that n corresponds to
    # This is the digit in the number that n is in
    digit = int(str(num)[digit_index])
    return digit

q = int(input())
for i in range(q):
    n = int(input())
    print(get_digit(n))
