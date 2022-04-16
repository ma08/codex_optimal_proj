

from collections import Counter
a = input()
b = input()
a = Counter(a)
b = Counter(b)
c = a & b
print(len(list(c.elements())))
