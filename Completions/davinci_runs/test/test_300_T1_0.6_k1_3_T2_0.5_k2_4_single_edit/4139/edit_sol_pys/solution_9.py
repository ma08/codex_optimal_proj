# -*- coding: utf-8 -*-


N = int(input())

def is_shichigosan(n):
    if '7' in n and '5' in n and '3' in n:
        for i in range(1, 10):
            if str(i) in n and i not in [3, 5, 7]:
                return False
        return True
    else:
        return False

count = 0
for i in range(1, N+1):
    if is_shichigosan(str(i)):
        count += 1

print(count)
