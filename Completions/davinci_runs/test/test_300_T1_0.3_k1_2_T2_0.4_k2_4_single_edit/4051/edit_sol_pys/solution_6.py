

def is_palindrome(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            return False
    return True


def palindrome_index(s):
    for i in range(len(s) // 2):
        if s[i] != s[len(s) - i - 1]:
            if is_palindrome(s[:i] + s[i + 1:]):
                return i
            else:
                return len(s) - i - 1
    return -1


t = int(input())

for _ in range(t):
    s = input()
    print(palindrome_index(s))
