

def greedy_inc_subseq(s):
    """
    Return the length of the longest increasing subsequence in arr.
    """
    last_element = s[0]
    last_index = 0
    for i in range(1, len(s)):
        if s[i] >= last_element:
            last_element = s[i]
            last_index = i
    return last_index + 1


if __name__ == "__main__":
    n = int(input())
    s = [int(x) for x in input().split()]
    print(greedy_inc_subseq(s))
