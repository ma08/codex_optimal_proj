

def isPalindrome(sub):
    for i in range(int(len(sub)/2)):
        if sub[i] != sub[-i-1]:
            return False
    return True

def isAnyPalindrome(a):
    for i in range(3, len(a)+1):
        for j in range(len(a)-i+1):
            if isPalindrome(a[j:j+i]):
                return True
    return False

t = int(input())
for _ in range(t):
    n = int(input())
    a = [int(x) for x in input().split()]
    if isAnyPalindrome(a):
        print("YES")
    else:
        print("NO")