

a = [int(x) for x in input().split()]

if sum(a) % 2 == 0 and all(x % 2 == 0 for x in a):
    print(1)
else:
    print(0)