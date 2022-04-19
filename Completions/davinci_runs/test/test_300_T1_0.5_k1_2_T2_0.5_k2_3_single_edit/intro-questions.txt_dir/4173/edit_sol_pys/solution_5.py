
"""
q = int(input())

for i in range(q):
    n, a, b = [int(x) for x in input().split()]
    
    min_bottles = n//2
    min_cost = min_bottles * b + (n%2)*a
    if a > b:
        min_cost = min(min_cost, (n//2)*a + (n%2)*b)
    
"""

def sum_of_digits(n):
    return sum([int(x) for x in str(n)])


n = int(input())

if n < 10:
    print(n)
else:
    digits = len(str(n))
    sum_digits = sum_of_digits(n)
    if sum_digits <= 9:
        print(digits*sum_digits)
    else:
        print(digits*9)
    print(min_cost)
