

# SOLUTION

# This is a very easy problem. The only thing to do is to calculate the number of digits in the block and then calculate the block number

def solve(k):
    # Calculate the number of digits in the block
    n = 1
    while n*(n+1)/2 < k:
        n += 1
    # Calculate the number of digits in the previous block
    prev_n = n - 1
    # Calculate the block number
    block_number = (k - prev_n*(prev_n+1)/2) // n
    # Calculate the number in the block
    number = (k - prev_n*(prev_n+1)/2) % n
    # Calculate the digit in the number
    digit = str(block_number+1)[number]
    return int(digit)

q = int(input())
for _ in range(q):
    k = int(input())
    print(solve(k))