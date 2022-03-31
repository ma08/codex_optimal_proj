
n = int(input())
a = list(map(int, input().split()))

def palindrome(n, a):
    if n == 1:
        return True
    if n % 2 == 0:
        if a[0] == a[n*n-1] and a[n-1] == a[n*n-n]:
            return palindrome(n-2, a[n:-n])
        return False
    else:
        if a[0] == a[n*n-1] == a[n*n//2]:
            return palindrome(n-2, a[n:-n])
        return False

if palindrome(n, a):
    print("YES")
    for i in range(n):
        print(*a[i*n:i*n+n])
else:
    print("NO")
