n, m = map(int, input().split())
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]


a.sort()
b.sort()

if a[-1] >= b[0]:
    print('War')
else:
    print('No War')
