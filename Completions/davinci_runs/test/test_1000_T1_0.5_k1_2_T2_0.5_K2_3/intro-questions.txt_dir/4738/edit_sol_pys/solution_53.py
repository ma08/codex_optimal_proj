

def k_periodic(s: str) -> int:
    """
    Find the period of a string.
    If a string has a period k, it is equal to itself if it is cut into k-length pieces and then concatenated.
    For example, "ababab" has a period of 3, because "ab" is repeated.
    "abab" has a period of 2, because "ab" is repeated.
    "ab" has a period of 1, because "a" is repeated.
    "a" has a period of 1, because "a" is repeated.
    "" has a period of 0, because "" is repeated.
    """
    k = 1
    while k < len(s):
        if s[:-k] == s[k:]:
            return k
        k += 1
    return len(s)

print(k_periodic(input()))
