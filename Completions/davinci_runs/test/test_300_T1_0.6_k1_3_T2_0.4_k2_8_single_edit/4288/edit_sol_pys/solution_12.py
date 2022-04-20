

a, b, c, d = map(int, input().split())

if a == b == c == d:
    print('No')
elif a == b or a == c or a == d or b == c or b == d or c == d:
    print('Yes')
else:
    print('No')
