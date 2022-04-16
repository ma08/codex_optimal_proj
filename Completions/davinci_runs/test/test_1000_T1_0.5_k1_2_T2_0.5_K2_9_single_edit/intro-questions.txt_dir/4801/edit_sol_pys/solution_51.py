

def greedy_inc_subseq(arr):
    """
    Return the length of the longest increasing subsequence in arr.
    """
    # Keep track of the last element in the increasing subsequence
    # (initially assume the first element is the last element)
    last_element = [arr[0]]
    for element in arr[1:]:  # for each element in the array
        if element > last_element[-1]:  # if element is greater than the last element in increasing subsequence
            last_element.append(element)  # append the element to the increasing subsequence
    return len(last_element)


if __name__ == "__main__":
    n = int(input())
    arr = [int(x) for x in input().split()]
    print(greedy_inc_subseq(arr))
