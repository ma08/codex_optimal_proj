

n = int(input())
for i in range(n):
    s = input()
    if len(s) != len(set(s)):
        print('No')
    elif ord(s[-1]) - ord(s[0]) + 1 == len(s):
        print('Yes')
    else:
        print('No')