

# Get input
a, b, k = map(int, input().split())

# Find the greatest common divisor
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Find the least common multiple
def lcm(a, b):
    return a * b // gcd(a, b)

# Find the K-th largest positive integer that divides both A and B
def find_kth(a, b, k):
    l = lcm(a, b)
    # Find the number of divisors of lcm(a, b)
    divisors = []
    for i in range(1, int(l**0.5) + 1):
        if l % i == 0:
            divisors.append(i)
            divisors.append(l // i)
    divisors.sort(reverse=True)
    # Find the K-th largest positive integer that divides both A and B
    return divisors[k-1]

print(find_kth(a, b, k))