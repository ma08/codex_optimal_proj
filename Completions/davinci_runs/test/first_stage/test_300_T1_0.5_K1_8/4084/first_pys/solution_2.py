
import math

def main():
    N, A, B = map(int, input().split())

    # print(N, A, B)

    # If N is less than A + B, then the number of blue balls will be N.
    if N < A + B:
        print(N)
        return

    # If N is greater than A + B, then the number of blue balls will be A.
    if N > A + B:
        print(A)
        return

    # If N is equal to A + B, then we will calculate the number of blue balls.
    # First, we will calculate the number of blue balls in the first A + B balls.
    # Then, we will calculate the number of blue balls in the first N balls.
    # The difference between the two numbers will be the number of blue balls in the first N balls.
    first_a_plus_b_blue_balls = 0
    for i in range(1, A + B + 1):
        first_a_plus_b_blue_balls += math.floor(i / (A + 1))
    # print(first_a_plus_b_blue_balls)

    first_n_blue_balls = 0
    for i in range(1, N + 1):
        first_n_blue_balls += math.floor(i / (A + 1))
    # print(first_n_blue_balls)

    print(first_n_blue_balls - first_a_plus_b_blue_balls)

if __name__ == '__main__':
    main()