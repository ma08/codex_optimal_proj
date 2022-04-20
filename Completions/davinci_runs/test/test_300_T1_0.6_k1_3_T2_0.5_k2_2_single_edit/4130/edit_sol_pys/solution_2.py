
#----Solution----
#----Solution----

n = int(input())
a = sorted([int(i) for i in input().split()])

set1 = set(a)

if len(set1) == len(a):
    print(len(a))
else:
    if len(set1) == 1:
        print(len(a) + 1)
    else:
        count = 0
        for i in range(len(a)):
            if a[i] != i + 1:
                count += 1
        print(len(a) - count)
