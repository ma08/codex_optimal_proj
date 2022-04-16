

import sys

# Set max recursion limit
sys.setrecursionlimit(100000)

def main():
    # Read input
    H, N, M = [int(i) for i in input().split()]
    A, B = 0, 0
    # Base case: height 1
    if H == 1:
        A = N
        B = M
    # Recursive case: height > 1
    else:
        # Calculate number of bricks in top layer of pyramid
        top_layer = 2 * H
        # Calculate number of bricks in bottom layer of pyramid
        bottom_layer = 2
        # Calculate number of layers of pyramid
        layers = H
        # Calculate number of bricks in top half of pyramid
        top_half = top_layer + bottom_layer
        # Calculate number of bricks in bottom half of pyramid
        bottom_half = top_layer + bottom_layer + 4 * (layers - 2)
        # Calculate number of bricks in whole pyramid of pyramid
        total_bricks = top_half + bottom_half
        # Calculate number of bricks in existing pyramid of pyramid
        existing_bricks = 2 * N + 4 * M
        # Calculate number of bricks needed for pyramid
        needed_bricks = total_bricks - existing_bricks
        # Calculate number of $2 \times 2$-bricks needed for pyramid
        A = needed_bricks // 2
        # Calculate number of $4 \times 2$-bricks needed for pyramid
        B = needed_bricks // 4
        # If $2 \times 2$-bricks needed is greater than $4 \times 2$-bricks needed for pyramid,
        # increase $2 \times 2$-bricks needed for pyramid by 1 and decrease $4 \times 2$-bricks needed for pyramid by 1
        if A > B:
            A += 1
            B -= 1
    # Print output
    print(A, B)

if __name__ == "__main__":
    main()
