

import sys
sys.setrecursionlimit(10**5)

def isPalindrome(n):
    if n == 0:
        return True
    else:
        return (n % 10 == n // 10**(len(str(n))-1)) and isPalindrome(n%10**(len(str(n))-1)//10)

a, b = map(int, input().split())

cnt = 0
for i in range(a, b+1):
    if isPalindrome(i):
        cnt += 1

print(cnt)
