
def solve(s):
    """
    >>> solve([1, 2, 3, 4, 5])
    [1, 2, 3, 4, 5]
    >>> solve([5, 4, 3, 2, 1])
    [1, 2, 3, 4, 5]
    >>> solve([3, 1, 2, 4, 5])
    [1, 2, 3, 4, 5]
    """
    for i in range(len(s)):
        min_index = i
        for j in range(i, len(s)):
            if s[j] < s[min_index]:
                min_index = j
        s[i], s[min_index] = s[min_index], s[i]
    return s


if __name__ == "__main__":
    s = [int(i) for i in input().split()]
    result = solve(s)
    print(result)
