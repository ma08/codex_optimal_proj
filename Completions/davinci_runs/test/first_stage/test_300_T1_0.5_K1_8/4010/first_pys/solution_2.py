


def isPalindrome(s):
    return s == s[::-1]


def checkForPalindrome(n, arr):
    for i in range(n - 2):
        for j in range(i + 3, n + 1):
            if isPalindrome(arr[i:j]):
                return True
    return False


for _ in range(int(input())):
    n = int(input())
    arr = input().split()
    print("YES" if checkForPalindrome(n, arr) else "NO")