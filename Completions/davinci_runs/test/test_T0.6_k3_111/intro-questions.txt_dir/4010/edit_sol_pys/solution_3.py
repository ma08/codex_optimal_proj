

def is_palindrome(arr):
    for i in range(0, int(len(arr)/2)):
        if arr[i] != arr[len(arr)-i-1]:
            return False
    return True

def main():
    t = int(input())
    for _ in range(0, t):
        n = int(input())
        a = list(map(int, input().split()))
        for i in range(0, n-1):
            for j in range(i+1, n):
                if is_palindrome(a[i:j]):
                    print("YES", i, j)
                    exit(0)
        print("NO")

main()
