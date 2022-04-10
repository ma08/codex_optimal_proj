

# SOLUTION
n = int(input())
a = list(map(int, input().split()))

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return (a * b) // gcd(a, b)

def lcm_of_list(a):
    return reduce(lcm, a)

def count_divisors(n):
    count = 0
    i = 1
    while i * i <= n:
        if n % i == 0:
            if n / i == i:
                count += 1
            else:
                count += 2
        i += 1
    return count

print(count_divisors(lcm_of_list(a)))