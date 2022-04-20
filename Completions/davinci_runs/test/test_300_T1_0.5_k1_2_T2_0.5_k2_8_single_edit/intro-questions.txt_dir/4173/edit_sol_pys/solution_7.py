

q = int(input())

for i in range(q):
    n = int(input())
    arr = [int(x) for x in input().split()]

    for x in arr:
        if x>0:
            print(x, end = " ")

    print()
