

def check(a, b, c):
    if b-a == c-b:
        print("YES")
    else:
        print("NO")


n = int(input())

if n == 1:
    print("NO")
elif n == 2:
    a, b = map(int, input().split())
    if b-a == 1:
        print("YES")
    else:
        print("NO")
else:
    a, b, c = map(int, input().split())
    check(a, b, c)
    for i in range(n-3):
        a, b, c = b, c, int(input())
        check(a, b, c)
