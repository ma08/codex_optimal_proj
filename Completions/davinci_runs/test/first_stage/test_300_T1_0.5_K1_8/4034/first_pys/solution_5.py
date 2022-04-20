

n = int(input())
s = input()

def check(s):
    for i in range(1, n):
        if s[i] < s[i - 1]:
            return False
    return True

def check2(s):
    for i in range(1, n):
        if s[i] == s[i - 1]:
            return False
    return True

if check(s):
    print("YES")
    print("0" * n)
    exit()

if check2(s):
    print("YES")
    print("01" * (n // 2) + "0" * (n % 2))
    exit()

print("NO")