

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if n < 3:
            print("NO")
        else:
            print("YES" if check_palindrome(n, a) else "NO")

def check_palindrome(n, a):
    for i in range(n - 2):
        if a[i] == a[i + 1] and a[i] == a[i + 2]:
            return True
    return False

if __name__ == "__main__":
    main()