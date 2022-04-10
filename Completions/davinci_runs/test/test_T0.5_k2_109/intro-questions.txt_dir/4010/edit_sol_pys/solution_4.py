


def is_palindrome(subsequence):
    for i in range(len(subsequence)):
        if subsequence[i] != subsequence[len(subsequence) - i - 1]:
            return False
    return True


def find_palindrome(a):
    for i in range(len(a) - 2):
        if is_palindrome(a[i:i + 3]):
            return True

    return False

def main():
    t = int(input())
    for i in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        if find_palindrome(a):
            print("YES")
        else:
            print("NO")


if __name__ == "__main__":
    main()
