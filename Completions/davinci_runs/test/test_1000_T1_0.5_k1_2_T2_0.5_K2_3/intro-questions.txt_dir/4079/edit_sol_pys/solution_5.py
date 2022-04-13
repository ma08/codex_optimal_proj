

# Solution

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for j in range(1, len(s)):
        if ord(s[j]) == ord(s[j - 1]) + 1:
            ok = False
            break
    if len(s) != len(set(s)) or len(s) > 26:
        ok = False
    print('Yes' if ok else 'No')
