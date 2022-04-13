from itertools import product
a = list(map(int, input().split()))
print(len(set(product(range(a[0]+1), range(a[1]+1), range(a[2]+1)))))
