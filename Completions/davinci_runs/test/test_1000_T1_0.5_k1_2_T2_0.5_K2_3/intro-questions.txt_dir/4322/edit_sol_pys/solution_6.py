n, m = [int(i) for i in input().split()]
a = [int(i) for i in input().split()]
b = [int(i) for i in input().split()]
if len(set(a).union(set(b))) == n:
    print('I become the guy.')
else:
    print('Oh, my keyboard!')
