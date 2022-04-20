

a, b, c = map(int, input().split())

if a == b:
    if a != c:
        print('No')
    else:
        print('Yes')
elif a == c:
    print('No')
elif b == c:
    print('No')
else:
    print('No')
