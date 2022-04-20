
S = input()

ans = 0
for i in range(len(S)):
    if S[i] == S[i-1]:
        ans += 1

def is_palindrome_with_one_change(S):
    if is_palindrome(S):
        return True
    for i in range(len(S)):
        if is_palindrome(S[:i] + S[i+1:]):
            return True
    return False

print(0 if is_palindrome_with_one_change(S) else 1)
