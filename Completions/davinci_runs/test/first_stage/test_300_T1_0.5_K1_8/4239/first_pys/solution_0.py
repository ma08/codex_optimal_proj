

import math

N = int(input())

n_min = 1
n_max = N

n = math.floor(N/2)

while True:
    if n_min == n_max:
        break
    elif n_max - n_min == 1:
        if n_min * n_min * n_min > N:
            n = n_min
        elif n_max * n_max * n_max > N:
            n = n_max
        else:
            n = n_max
        break
    elif n * n * n > N:
        n_max = n
        n = math.floor((n_min + n_max) / 2)
    else:
        n_min = n
        n = math.floor((n_min + n_max) / 2)

#print(n)

n_min = n
n_max = n

while n_min * n_min * n_min > N:
    n_min -= 1

while (n_max + 1) * (n_max + 1) * (n_max + 1) <= N:
    n_max += 1

#print(n_min, n_max)

n_min_list = []
n_max_list = []

for i in range(n_min, 0, -1):
    if N - i * i * i >= 0:
        n_min_list.append(N - i * i * i)

for i in range(n_max, 0, -1):
    if N - i * i * i >= 0:
        n_max_list.append(N - i * i * i)

#print(n_min_list)
#print(n_max_list)

count_min = 0
count_max = 0

for i in n_min_list:
    if i == 0:
        break
    elif i == 1:
        count_min += 1
        break
    elif i == 6:
        count_min += 1
        break
    elif i == 9:
        count_min += 1
        break
    else:
        count_min += 1
        n_min_list.append(i-1)
        n_min_list.append(i-6)
        n_min_list.append(i-9)

for i in n_max_list:
    if i == 0:
        break
    elif i == 1:
        count_max += 1
        break
    elif i == 6:
        count_max += 1
        break
    elif i == 9:
        count_max += 1
        break
    else:
        count_max += 1
        n_max_list.append(i-1)
        n_max_list.append(i-6)
        n_max_list.append(i-9)

#print(count_min)
#print(count_max)

print(min(count_min, count_max))