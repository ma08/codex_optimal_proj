

a, b = map(int, input().split())
s = input()

if len(s) == a + b + 1 and s[a] == '-' and s[:a].isdigit() and s[a+1:].isdigit() and a>0 and b>0:
    print('Yes')
else:
    print('No')
