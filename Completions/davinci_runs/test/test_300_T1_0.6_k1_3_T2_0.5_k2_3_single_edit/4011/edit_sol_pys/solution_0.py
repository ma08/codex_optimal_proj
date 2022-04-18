

def solve():
    n = int(input())
    a = input()
    f = list(map(int, input().split()))

    # print(n, a, f)

    # Transform a into an array of ints
    a = list(map(int, list(a)))
    # print(a)

    # Create an empty array to store the result
    b = [0] * n

    # Iterate through the array a
    for i in range(n):
        # Transform each element of a using the mapping f
        b[i] = f[a[i]]

    # print(b)

    # Create an empty array to store the indices of the maximum elements of b
    max_indices = []

    # Iterate through the array b
    for i in range(n):
        # If the element of b at index i is greater than the elements of b at previous indices,
        # then store the index i
        if i == 0 or b[i] > b[max_indices[0]]:
            max_indices = [i]
        # If the element of b at index i is equal to the elements of b at previous indices,
        # then also store the index i
        elif b[i] == b[max_indices[0]]:
            max_indices.append(i)

    # print(max_indices)

    # If there is only one index of the maximum elements of b, then no change is required
    if len(max_indices) == 1:
        print(''.join(map(str, b)))
    # If there are multiple indices of the maximum elements of b, then we need to choose
    # the segment that contains the maximum elements of b, and transform that segment
    # using the mapping f
    else:
        # Find the minimum index of the maximum elements of b
        min_index = max_indices[0]
        for i in range(1, len(max_indices)):
            if max_indices[i] < min_index:
                min_index = max_indices[i]

        # print(min_index)

        # Find the maximum index of the maximum elements of b
        max_index = max_indices[0]
        for i in range(1, len(max_indices)):
            if max_indices[i] > max_index:
                max_index = max_indices[i]

        # print(max_index)

        # Transform the segment of b that contains the maximum elements of b using the mapping f
        for i in range(min_index, max_index + 1):
            b[i] = f[b[i]]

        print(''.join(map(str, b)))


if __name__ == "__main__":
    solve()
