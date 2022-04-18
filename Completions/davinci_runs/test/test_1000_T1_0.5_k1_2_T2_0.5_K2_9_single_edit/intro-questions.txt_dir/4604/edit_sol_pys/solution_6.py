

import sys

def main():
    # Read from standard input
    N = int(sys.stdin.readline())
    A = list(map(int, sys.stdin.readline().split()))

    # Check if each person's report is consistent with the others
    for i in range(N):
        if abs(i - A[i]) > 1:
            print(0)
            sys.exit()

    # Initialize a list of the number of people to the left of each person
    # and the number of people to the right of each person
    left = [0] * N
    right = [0] * N

    # Count the number of people to the left of each person
    for i in range(N):
        for j in range(N):
            if j < i:
                left[i] += A[j]
            elif j > i:
                left[i] += (N - 1 - A[j])

    # Count the number of people to the right of each person
    for i in range(N):
        for j in range(N):
            if j < i:
                right[i] += (N - 1 - A[j])
            elif j > i:
                right[i] += A[j]

    # Initialize a list to keep track of the number of ways to order the people
    # and the number of people we have ordered
    num_ways = [0] * N
    num_ordered = 0

    # Order the people
    while num_ordered < N:
        # Find the first person that has not been ordered
        i = left.index(0)

        # Add this person to the ordered list
        num_ways[num_ordered] = i + 1
        num_ordered += 1

        # Subtract the number of people to the left of this person from everyone else
        for j in range(N):
            left[j] -= A[i]
            right[j] -= (N - 1 - A[i])

        # Remove this person from the list
        left[i] = -1
        right[i] = -1

    # Print the number of ways to order the people
    print(num_ways[0])


if __name__ == "__main__":
    main()
