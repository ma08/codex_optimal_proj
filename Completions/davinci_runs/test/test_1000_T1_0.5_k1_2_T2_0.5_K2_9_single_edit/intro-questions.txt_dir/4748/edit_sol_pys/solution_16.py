

import sys

# Set max recursion limit
sys.setrecursionlimit(100000)

def main():
    # Read input
    H, N, M = [int(i) for i in input().split()]
    a, b = 0, 0
    # Base case: height 1
    if H == 1:
        a = N
        b = M
    # Recursive case: height > 1
    else:
        # Calculate number of bricks in top layer
        top_layer = 2 * h
        # Calculate number of bricks in bottom layer
        bottom_layer = 2
        # Calculate number of layers
        layers = h
        # Calculate number of bricks in top half
        top_half = top_layer + bottom_layer
        # Calculate number of bricks in bottom half
        bottom_half = top_layer + bottom_layer + 4 * (layers - 2)
        # Calculate number of bricks in whole pyramid
        total_bricks = top_half + bottom_half
        # Calculate number of bricks in existing pyramid
        existing_bricks = 2 * N + 4 * M
        # Calculate number of bricks needed
        needed_bricks = total_bricks - existing_bricks
        # Calculate number of $2 \times 2$-bricks needed
        a = needed_bricks // 2
        # Calculate number of $4 \times 2$-bricks needed
        b = needed_bricks // 4
        # If $2 \times 2$-bricks needed is greater than $4 \times 2$-bricks needed,
        # increase $2 \times 2$-bricks needed by 1 and decrease $4 \times 2$-bricks needed by 1
        if a > b:
            a += 1
            b -= 1
    # Print output
    print(A, B)

if __name__ == "__main__":
    main()
