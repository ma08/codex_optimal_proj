

n, w = map(int, input().split())
a = [int(x) for x in input().split()]

if w == 1:
    if len(set(a)) == 1:
        print(1)
    else:
        print(0)
else:
    if len(set(a)) == 1:
        print(w+1)
    else:
        print(0)