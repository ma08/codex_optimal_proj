

def greedy_inc_subsequence(arr):
    """
    Return the length of the longest increasing subsequence in arr.
    """
    # Keep track of the last element in the increasing subsequence
    # (initially assume the first element is the last element)
    # Keep track of the length of the longest increasing subsequence
    last_element = arr[0]
    # Iterate through the array, checking if each element is greater than
    # the last element
    length = 1
        # If it is, update last element and increment length
    for element in arr[1:]:
        if element > last_element:
            last_element = element
            length += 1
    return length


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(greedy_inc_subsequence(arr))
