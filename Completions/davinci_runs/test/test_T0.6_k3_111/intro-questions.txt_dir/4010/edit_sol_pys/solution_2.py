

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
        if is_palindrome(a):
            print("YES")
        else:
            print("NO")

main()
