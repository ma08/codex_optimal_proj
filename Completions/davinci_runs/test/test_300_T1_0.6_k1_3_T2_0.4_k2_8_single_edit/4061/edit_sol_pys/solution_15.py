

def findLongestSubstring(s, t):
    """
    :type s: str
    :type t: str
    :rtype: int
    """
    if len(s) == 0 or len(t) == 0:
        return 0

    if len(s) == 1:
        return 0 if s == t else 1

    if len(t) == 1:
        return 0 if t in s else 1

    left, right = 0, len(s)
    while right - left > 2:
        mid = (left + right) // 2
        if t in s[mid:]:
            right = mid
        elif t in s[:mid]:
            left = mid
        else:
            break

    if t in s[right:]:
        return len(s) - right + 1
    elif t in s[left:]:
        return len(s) - left + 1
    else:
        return 0

if __name__ == "__main__":
    s = raw_input()
    t = raw_input()
    print findLongestSubstring(s, t)
