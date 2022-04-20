

import math

def find_min_num_of_packages(n, k):
    return math.ceil(n / k)

t = int(input())

for i in range(t):
    n, k = map(int, input().split())
    print(find_min_num_of_packages(n, k))