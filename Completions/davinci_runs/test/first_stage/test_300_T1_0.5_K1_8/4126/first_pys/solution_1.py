


def is_palindrome(s):
    return s == s[::-1]


def is_strong_palindrome(s):
    return is_palindrome(s) and is_palindrome(s[:len(s) // 2]) and is_palindrome(s[len(s) // 2 + 1:])


s = input()
print('Yes' if is_strong_palindrome(s) else 'No')