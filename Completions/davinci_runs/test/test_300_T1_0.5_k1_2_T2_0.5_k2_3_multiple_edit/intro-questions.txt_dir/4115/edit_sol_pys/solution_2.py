

"""
解説通り

・入力文字列が回文かどうかを判定する関数
・入力文字列の各文字を1文字ずつ変更して回文にできるかどうかを判定する関数

"""

S = input()

def is_palindrome(s):
    if len(s) <= 1:
        return True
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def is_palindrome_with_one_change(s):
    if is_palindrome(s):
        return True
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i+1:]):
            return True
    return False

print(0 if is_palindrome_with_one_change(S) else 1)
