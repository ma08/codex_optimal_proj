

def is_palindrome(s):
    return s == s[::-1]

S = input()

if is_palindrome(S) and is_palindrome(S[:(len(S)-1)//2]) and is_palindrome(S[(len(S)+3)//2-1:]):
    print("Yes")
else:
    print("No")