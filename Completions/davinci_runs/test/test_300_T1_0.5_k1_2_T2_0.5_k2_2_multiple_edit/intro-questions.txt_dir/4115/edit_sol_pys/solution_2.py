

"""
解説放送より https://youtu.be/Qx1q3sDV7Lc?t=10553

・入力文字列が回文かどうかを判定する関数
・入力文字列の各文字を1文字ずつ変更して回文にできるかどうかを判定する関数

"""

S = input()

def is_palindrome(S):
    if len(S) <= 1:
        return True
    return S[0] == S[-1] and is_palindrome(S[1:-1])

def is_palindrome_with_one_change(s):
    if is_palindrome(s):
        return True 
    for i in range(len(s)):
        if is_palindrome(s[:i] + s[i+1:]):
            return True
    return False 

print(0 if is_palindrome_with_one_change(S) else 1)
