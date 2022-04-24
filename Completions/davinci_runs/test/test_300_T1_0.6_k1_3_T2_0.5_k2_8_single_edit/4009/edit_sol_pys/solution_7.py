
n, x, y = map(int, input().split())
s = input()

if int(s[x-y:x]) == 0 and y > x:
    print(1)
else:
    print(0)
