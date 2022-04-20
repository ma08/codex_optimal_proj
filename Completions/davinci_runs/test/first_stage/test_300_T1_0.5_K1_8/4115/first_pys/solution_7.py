

s = input()

def palindrome(s):
    if len(s) == 1:
        return 0
    elif len(s) == 2:
        if s[0] == s[1]:
            return 0
        else:
            return 1
    else:
        if s[0] == s[-1]:
            return palindrome(s[1:-1])
        else:
            return min(palindrome(s[1:]), palindrome(s[:-1])) + 1

print(palindrome(s))