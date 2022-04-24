
k = int(input())
s = input()

if len(s) <= k:
    print(s, end='')
else:
    print(s[:k] + "...", end='')
