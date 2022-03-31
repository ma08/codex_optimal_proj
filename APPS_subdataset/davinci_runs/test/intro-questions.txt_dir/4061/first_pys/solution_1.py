

"""
Approach:
1. Find all the indices where the character in t is found in s
2. Now, the elements between these indices(inclusive) should be removed, so that t is a subsequence of s
3. Now, we need to find the maximum subarray sum(in this case it will be the maximum contiguous subsequence that can be removed)
"""

def max_contiguous_subarray_sum(arr):
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, len(arr)):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    return max_sum

def main():
    s = input().strip()
    t = input().strip()
    indices = []
    for i in range(len(s)):
        if s[i] == t[0]:
            indices.append(i)
    t = t[1:]
    for c in t:
        new_indices = []
        for j in range(len(indices)):
            for i in range(indices[j] + 1, len(s)):
                if s[i] == c:
                    new_indices.append(i)
                    break
        indices = new_indices
    differences = []
    for i in range(1, len(indices)):
        differences.append(indices[i] - indices[i - 1])
    print(max_contiguous_subarray_sum(differences))

if __name__ == '__main__':
    main()