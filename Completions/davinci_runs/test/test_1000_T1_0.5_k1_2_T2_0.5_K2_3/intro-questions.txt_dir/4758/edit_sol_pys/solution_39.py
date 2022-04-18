
from itertools import product
a = list(map(int, input().split())) # переводим все в числовой формат
print(len(set(product(range(a[0]), range(a[1]), range(a[2])))))
