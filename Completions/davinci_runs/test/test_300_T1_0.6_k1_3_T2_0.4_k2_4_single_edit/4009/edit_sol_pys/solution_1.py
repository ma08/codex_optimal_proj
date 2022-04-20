
n, x, y = [int(x) for x in input().split()]
s = input()

if int(s[x-y:x]) == 0 and x < y:
    print(1)
else:
    print(0)
