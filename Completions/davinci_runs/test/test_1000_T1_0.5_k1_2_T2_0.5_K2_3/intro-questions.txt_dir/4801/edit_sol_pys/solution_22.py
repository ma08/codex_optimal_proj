

def greedy_inc_subsequence(arr):
    """
    Return the length of the longest increasing subsequence in arr.
    """
    # Keep track of the last element in the increasing subsequence
    # (initially assume the first element is the last element)
    last_element = 0
    length = 1
    for element in arr:
        if element > last_element:
            last_element = element
            length += 1
    return length


if __name__ == "__main__":
    arr = [3, 2, 6, 4, 5, 1]
    print(greedy_inc_subsequence(arr))
