

def is_palindrome(s):
    return s == s[::-1]

a = input()
b = input()
print("YES" if is_palindrome(a + b) else "NO")
