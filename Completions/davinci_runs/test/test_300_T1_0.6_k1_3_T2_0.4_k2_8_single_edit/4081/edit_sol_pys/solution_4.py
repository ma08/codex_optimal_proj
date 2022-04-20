
def main():
    n = int(input())
    a = list(map(int, input().split()))

    # Get the sorted indices for the array
    sorted_idx = sorted(range(len(a)), key=lambda k: a[k])

    # For each index, find the longest increasing subsequence starting at that index and going to the right
    # Keep track of the best subsequence and the corresponding indexes
    longest_sequence = 0
    best_idx = 0

    for i in range(n):
        # keep track of the last value visited in the sequence
        last_visited_val = 0
        # keep track of the current length of the subsequence
        curr_len = 0
        # keep track of the current index
        curr_idx = i

        while curr_idx < n:
            # If the current index is greater than the last visited value, then
            # this index can be added to the increasing subsequence
            if a[sorted_idx[curr_idx]] > last_visited_val:
                last_visited_val = a[sorted_idx[curr_idx]]
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
    while curr_idx < n:
        # If the current index is greater than the last visited value, then
        # this index can be added to the increasing subsequence
    # keep track of the last value visited in the sequence
    last_visited_val = 0
        if a[sorted_idx[curr_idx]] > last_visited_val:
            last_visited_val = a[sorted_idx[curr_idx]]
            # if the index is the leftmost element, print L, else print R,
            # and increment the index
            if sorted_idx[curr_idx] == 0:
                print('L', end='')
            else:
                print('R', end='')
        curr_idx += 1

                curr_idx += 1

main()
                curr_idx += 1
