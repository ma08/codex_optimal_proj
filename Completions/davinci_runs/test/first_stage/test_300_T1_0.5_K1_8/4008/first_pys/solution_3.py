


def main():
    n, k = [int(x) for x in input().split()]
    a = [int(x) for x in input().split()]

    # We can color each distinct value in the array with a different color,
    # and all other values with the same color. In this way, we can always
    # color all distinct values with $k$ colors.
    #
    # To see this, consider the following example with $k=2$:
    #
    #   a = [1, 2, 2, 3]
    #
    # We can color the distinct values with different colors, and color all
    # other values with the same color:
    #
    #   a = [1, 2, 2, 3]
    #   c = [1, 2, 2, 1]
    #
    # This coloring has the following properties:
    #
    #   1. Each element of the array is colored in some color.
    #
    #   2. For each $i$ from $1$ to $k$ there is at least one element colored
    #      in the $i$-th color in the array.
    #
    #   3. For each $i$ from $1$ to $k$ all elements colored in the $i$-th color
    #      are distinct.
    #
    # Now, consider the following example with $k=3$:
    #
    #   a = [1, 2, 2, 3]
    #
    # We can color the distinct values with different colors, and color all
    # other values with the same color:
    #
    #   a = [1, 2, 2, 3]
    #   c = [1, 2, 2, 3]
    #
    # This coloring has the following properties:
    #
    #   1. Each element of the array is colored in some color.
    #
    #   2. For each $i$ from $1$ to $k$ there is at least one element colored
    #      in the $i$-th color in the array.
    #
    #   3. For each $i$ from $1$ to $k$ all elements colored in the $i$-th color
    #      are distinct.
    #
    # In general, we can color the distinct values with different colors, and
    # color all other values with the same color. This coloring has the
    # following properties:
    #
    #   1. Each element of the array is colored in some color.
    #
    #   2. For each $i$ from $1$ to $k$ there is at least one element colored
    #      in the $i$-th color in the array.
    #
    #   3. For each $i$ from $1$ to $k$ all elements colored in the $i$-th color
    #      are distinct.

    # If there are more than $k$ distinct values, then the coloring is
    # impossible.
    if len(set(a)) > k:
        print("NO")
    else:
        # Otherwise, color each distinct value with a different color.
        c = [0] * n
        for i, x in enumerate(a):
            if c[i] == 0:
                c[i] = x
        # Color all other values with the same color.
        for i, x in enumerate(a):
            if c[i] == 0:
                c[i] = 1
        # Print the answer.
        print("YES")
        print(" ".join(str(x) for x in c))


if __name__ == "__main__":
    main()