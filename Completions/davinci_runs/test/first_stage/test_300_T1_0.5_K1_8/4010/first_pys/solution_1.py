

def isPalindrome(a):
    n = len(a)
    for i in range(n//2):
        if a[i] != a[n - i - 1]:
            return False
    return True

def isPalindromeSubsequence(a):
    n = len(a)
    for i in range(n - 2):
        for j in range(i + 2, n + 1):
            if isPalindrome(a[i:j]):
                return True
    return False

t = int(input())
for i in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    if isPalindromeSubsequence(a):
        print("YES")
    else:
        print("NO")