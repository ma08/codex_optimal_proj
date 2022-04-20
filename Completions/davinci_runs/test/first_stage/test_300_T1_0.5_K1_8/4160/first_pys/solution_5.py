

import math

def calculate_years_to_reach(x):
    years = 1
    balance = 100
    while balance < x:
        balance = math.floor(balance * 1.01)
        years += 1
    return years

x = int(input())
print(calculate_years_to_reach(x))