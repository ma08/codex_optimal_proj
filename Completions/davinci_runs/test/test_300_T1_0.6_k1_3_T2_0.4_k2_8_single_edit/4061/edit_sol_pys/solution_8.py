


def findLongestSubstring(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) == len(t):
        return 0

    left, right = 0, len(s) - 1
    while right - left > 1:
        mid = (left + right) // 2
        if all(c in s[mid:] for c in t):
            left = mid
        else:
            right = mid

    if all(c in s[right:] for c in t):
        return len(s) - right
    else:
        return len(s) - left


if __name__ == "__main__":
    s = raw_input()
    t = raw_input()
    print findLongestSubstring(s, t)
