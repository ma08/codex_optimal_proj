


S = input()

def is_palindrome(s):
    if len(s) <= 1:
        return True 
    return s[0] == s[-1] and is_palindrome(s[1:-1])

def is_palindrome_with_one_change(S):
    if is_palindrome(S):
        return True
    for i in range(len(S)):
        if is_palindrome(S[:i] + S[i+1:]):
            return True
    return False

print(0 if is_palindrome_with_one_change(S) else 1)
