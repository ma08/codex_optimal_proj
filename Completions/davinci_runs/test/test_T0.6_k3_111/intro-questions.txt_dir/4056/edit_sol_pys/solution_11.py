
n = int(input())
arr = list(map(int, input().split()))
import math

def factorize(num):
    factors = []
    while num > 1:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                factors.append(i)
                num //= i
                break
        else:
            factors.append(num)
            break
    return factors

def factorize_efficient(num):
    factors = []
    while num % 2 == 0:
        factors.append(2)
        num //= 2
    for i in range(3, int(math.sqrt(num)) + 1, 2):
        while num % i == 0:
            factors.append(i)
            num //= i
    if num > 1:
        factors.append(num)
    return factors

def common_factors(arr):
    factor_dict = {}
    for num in arr:
        factors = factorize_efficient(num)
        for factor in factors:
            factor_dict[factor] = factor_dict.get(factor, 0) + 1

    max_occur = max(factor_dict.values())
    return max_occur


print(common_factors(arr))
