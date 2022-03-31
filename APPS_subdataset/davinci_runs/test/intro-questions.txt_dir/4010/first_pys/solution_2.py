

def isPalindrome(arr):
    for i in range(0, int(len(arr)/2)):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True

def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        for i in range(0, n):
            for j in range(0, n-i-1):
                if isPalindrome(a[i:j+1]):
                    print("YES")
                    break
        print("NO")

main()