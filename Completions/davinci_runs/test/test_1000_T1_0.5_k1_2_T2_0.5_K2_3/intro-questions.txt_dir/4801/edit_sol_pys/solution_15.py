

def greedy_inc_subseq(sequence):
    """
    Return the length of the longest increasing subsequence in sequence.
    """
    # Keep track of the last element in the increasing subsequence (initially
    # assume the first element is the last element)
    last_element, length = sequence[0], 1
    for element in sequence[1 :]:
        if element > last_element:  # If the current element is larger than the
            # last element, then it must be part of the increasing subsequence
            last_element = element  # Update the last element
            length += 1  # Update the length of the increasing subsequence
    return length  # Return the length of the increasing subsequence


if __name__ == "__main__":
    n = int(input())
    sequence = [int(x) for x in input().split()]
    print(greedy_inc_subseq(sequence))
