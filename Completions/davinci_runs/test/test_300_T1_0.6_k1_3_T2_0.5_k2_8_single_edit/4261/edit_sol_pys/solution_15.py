a = int(input())
b = int(input())
c = int(input())

a, b, c = map(int, input().split())

while 1:
    if a < b + c:
        print(b + c - a)
        exit()
    else:
        print(0)
        exit()
