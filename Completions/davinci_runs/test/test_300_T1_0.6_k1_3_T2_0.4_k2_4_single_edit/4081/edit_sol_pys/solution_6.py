


def main():
    n = int(input())
    a = list(map(int, input().split()))

    # Get the reverse sorted indices for the array
    r_sorted_idx = sorted(range(len(a)), key=lambda k: a[k])
    r_sorted_idx.reverse()

    # For each index, find the longest increasing subsequence starting at that index
    # Keep track of the best subsequence and the corresponding indexes
    longest_sequence = 0
    best_idx = 0

    for i in range(n):
        # keep track of the last index visited in the sequence
        last_visited_idx = 0
        # keep track of the current length of the subsequence
        curr_len = 0
        # keep track of the current index
        curr_idx = i

        while curr_idx < n:
            # If the current index is greater than the last visited index, then
            # this index can be added to the increasing subsequence
            if r_sorted_idx[curr_idx] > last_visited_idx:
                last_visited_idx = r_sorted_idx[curr_idx]
                curr_len += 1
            curr_idx += 1

        # If the current subsequence is longer than the previous best, then
        # update the best subsequence and the corresponding indexes
        if curr_len > longest_sequence:
            longest_sequence = curr_len
            best_idx = i

    # Print out the length of the longest subsequence
    print(longest_sequence)

    curr_idx = best_idx
    last_visited_idx = 0
    while curr_idx < n:
        # If the current index is greater than the last visited index, then
        # this index can be added to the increasing subsequence
        if r_sorted_idx[curr_idx] > last_visited_idx:
            last_visited_idx = r_sorted_idx[curr_idx]
            # if the index is the leftmost element, print L, else print R
            if last_visited_idx == 0:
                print('L', end='')
            else:
                print('R', end='')
        curr_idx += 1


main()
