

def isPalindrome(subsequence):
    for i in range(len(subsequence)):
        if subsequence[i] != subsequence[len(subsequence) - i - 1]:
            return False
    return True

def findPalindrome(a):
    for i in range(len(a) - 2):
        if isPalindrome(a[i:i+3]):
            return True
    return False

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if findPalindrome(a):
            print("YES")
        else:
            print("NO")

if __name__ == "__main__":
    main()