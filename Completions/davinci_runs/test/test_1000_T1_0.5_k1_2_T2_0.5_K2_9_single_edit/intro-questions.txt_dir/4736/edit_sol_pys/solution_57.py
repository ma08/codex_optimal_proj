


def is_valid(s):
    """
    Returns true if the string is a valid variable name, false otherwise.
    """
    if s[0].isdigit() or not s[0].isalpha():
        return False
    for i in range(1, len(s)):
        if not (s[i].isdigit() or s[i].isalpha() or s[i] == '_'):
            return False
    return True


def longest_valid_variable(s):
    """
    Returns the longest valid variable name that can be formed from the string s.
    """
    longest = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_valid(s[i:j]) and len(s[i:j]) > len(longest):
                longest = s[i:j]
    return longest


def longest_valid_variable_with_keywords(s):
    """
    Returns the longest valid variable name that can be formed from the string s,
    but does not match any of the keywords in the list keywords.
    """
    longest = ''
    for i in range(len(s)):
        for j in range(i + 1, len(s) + 1):
            if is_valid(s[i:j]) and len(s[i:j]) > len(longest) and s[i:j] not in keywords:
                longest = s[i:j]
    return longest
