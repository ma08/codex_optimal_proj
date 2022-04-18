

def greedy_inc_subseq(sequence):
    """
    Return the length of the longest increasing subsequence in sequence.
    """
    # Keep track of the last element in the increasing subsequence
    # (initially assume the first element is the last element)
    last_element = sequence[0]
    length = 1
    for element in sequence[1:]:
        if element > last_element:
            last_element = element
            length += 1
    return length


if __name__ == "__main__":
    n = int(input())
    seq = [int(x) for x in input().split()]
    print(greedy_inc_subseq(seq))
