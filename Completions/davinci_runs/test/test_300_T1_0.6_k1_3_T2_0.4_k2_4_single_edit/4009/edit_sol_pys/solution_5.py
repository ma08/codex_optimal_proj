

n, x, y = [int(x) for x in input().split()]
s = input()

if int(s[x-y:x]) == 0 and s[x-y-1] == '1':
    print(1)
else:
    print(0)
