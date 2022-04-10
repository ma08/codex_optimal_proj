

def isPalindrome(arr):
    for i in range(len(arr)//2):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True

def isPalindromeSubsequence(arr):
    for i in range(len(arr)-2):
        for j in range(i+2,len(arr)+1):
            if isPalindrome(arr[i:j]):
                return True
    return False

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int,input().split()))
        if isPalindromeSubsequence(arr):
            print("YES")
        else:
            print("NO")

main()