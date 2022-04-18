
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a == b == c == d:
    print('Yes')
elif a == b and c == d:
    print('Yes')
elif a == c and b == d:
    print('Yes')
elif a == d and b == c:
    print('Yes')
else: print('No')
