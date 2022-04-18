

def check_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

n = int(input())

print(check_palindrome(n))
