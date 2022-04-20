

import math

def factors(n):
    return set(reduce(list.__add__, ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

n = input()
nums = map(int, raw_input().split())
factors_per_num = [factors(num) for num in nums]
common_factors = factors_per_num[0].intersection(*factors_per_num[1:])
print len(common_factors)