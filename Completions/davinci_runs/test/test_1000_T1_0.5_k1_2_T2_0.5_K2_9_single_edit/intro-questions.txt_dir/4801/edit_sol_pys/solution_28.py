

def greedy_inc_subseq(arr):
    """
    Return the length of the longest increasing subsequence in arr.
    """
    # Keep track of the last element in the increasing subsequence
    # (initially assume the first element is the last element)
    last_element = arr[0] # O(1)
    length = 1
    for element in arr[1:]: # O(n)
        if element > last_element:
            last_element = element # O(1)
            length += 1
    return length # O(1)

# Total runtime: O(n)


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(greedy_inc_subseq(arr))
