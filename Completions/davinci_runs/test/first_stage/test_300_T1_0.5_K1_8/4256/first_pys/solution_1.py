

a, b, c = map(int, input().split())

if b >= a:
    if b % a == 0:
        print(min(b//a, c))
    else:
        print(min(b//a+1, c))
else:
    print(min(b//a, c))