

def gcd(a, b):  # function to find greatest common divisor
    while b:
        a, b = b, a % b
    return a

a, b, c = [int(x) for x in input().split()]

g = gcd(gcd(a, b), c)  # finding greatest common divisor

print(min(a//g, b//g, c//g)*7)  # printing minimum days
