

# Solution

n = int(input())

for i in range(n):
    s = input()
    ok = True
    for i in range(1, len(s)):
        if ord(s[i]) == ord(s[i - 1]) + 1:
            ok = False
            break
    if len(s) != len(set(s)):
        ok = False

    print('Yes' if ok else 'No')
