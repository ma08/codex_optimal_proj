
# Solution

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for j in range(1, len(s) - 1):
        if ord(s[j]) >= ord(s[j - 1]) and ord(s[j]) <= ord(s[j + 1]):
            if ord(s[j]) == ord(s[j - 1]) + 1:
                ok = False
                break
        if len(s) != len(set(s)):
        ok = False
    print('Yes' if ok else 'No')
