

from collections import Counter

def can_make_palindrome(S):
    count = Counter(S)
    odd_count = 0
    for v in count.values():
        if v % 2 == 1:
            odd_count += 1
    return odd_count <= 1

S = input()
print("Yes" if can_make_palindrome(S) else "No")
