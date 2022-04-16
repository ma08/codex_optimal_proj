

# Solution 1

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for j in range(1, len(s)):
        if ord(s[j]) == ord(s[j - 1]) + 1:
            ok = False
            break
    if len(s) != len(set(s)):
        ok = False

# Solution 2

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for j in range(1, len(s)):
        if ord(s[j]) == ord(s[j - 1]) + 1:
            ok = False
            break
    if len(s) != len(set(s)):
        ok = False
    print('Yes' if ok else 'No')

# Solution 3

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for j in range(1, len(s)):
        if ord(s[j]) == ord(s[j - 1]) + 1:
            ok = False
            break
    if len(s) != len(set(s)):
        ok = False
    print('Yes' if ok else 'No')

# Solution 4

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for j in range(1, len(s)):
        if ord(s[j]) == ord(s[j - 1]) + 1:
            ok = False
            break
    if len(s) != len(set(s)):
        ok = False
    print('Yes' if ok else 'No')
    print('Yes' if ok else 'No')
