
a1, a2, a3 = map(int, input().split())  # map(function, iterable) 
if sum([a1, a2, a3]) >= 22:
    print('bust')
else:
    print('win')
