


def main():
    s = input()
    t = input()

    # t = subsequence of s
    # find the longest substring of s that is not a subsequence of t
    # can be done by finding the longest substring of s that is a subsequence of t
    # and subtracting the length of this substring from the length of s
    # longest substring of s that is a subsequence of t is the same as the
    # longest substring of s that is a subsequence of t and a substring of s

    # make a list of indices for each character in t
    indices = {}
    for i, c in enumerate(t):
        if c in indices:
            indices[c].append(i)
        else:
            indices[c] = [i]
    
    # for each character in s, if it is in t, find the index of the next occurrence of this character in t
    # that is after the index of the last occurrence of this character in t
    # if there is no next occurrence, use the index of the last occurrence
    next_indices = []
    last_index = -1
    for c in s:
        if c in indices:
            next_index = -1
            for i in indices[c]:
                if i > last_index:
                    next_index = i
                    break
            if next_index == -1:
                next_index = indices[c][-1]
            next_indices.append(next_index)
            last_index = next_index
    
    # for each index in next_indices, find the length of the longest increasing subsequence
    # ending at this index
    # the answer is the length of s minus the longest increasing subsequence
    # the longest increasing subsequence is the longest substring of s that is a subsequence of t
    
    # longest_increasing_subsequence[i] = length of longest increasing subsequence ending at index i
    longest_increasing_subsequence = [1] * len(next_indices)
    for i in range(1, len(next_indices)):
        for j in range(i):
            if next_indices[j] < next_indices[i]:
                longest_increasing_subsequence[i] = max(longest_increasing_subsequence[i], longest_increasing_subsequence[j] + 1)
    print(len(s) - max(longest_increasing_subsequence))


if __name__ == "__main__":
    main()