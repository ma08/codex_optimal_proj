

import random
n = int(input())

a = [random.randint(1, n) for i in range(n)]

print(n)

print(*a)
