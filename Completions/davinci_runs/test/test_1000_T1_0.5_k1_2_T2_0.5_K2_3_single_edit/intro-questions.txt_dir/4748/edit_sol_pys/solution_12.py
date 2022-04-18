
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
        A, B = calculate_bricks(H, N, M)
    # Print output
    print(A, B)

if __name__ == "__main__":
    main()
