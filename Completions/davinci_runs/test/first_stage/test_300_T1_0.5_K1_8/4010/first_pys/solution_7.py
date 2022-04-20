


def is_palindrome(a):
    return a == a[::-1]


def is_palindrome_subsequence(a):
    n = len(a)
    for i in range(n):
        for j in range(i + 2, n + 1):
            if is_palindrome(a[i:j]):
                return True
    return False


if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        print('YES' if is_palindrome_subsequence(a) else 'NO')