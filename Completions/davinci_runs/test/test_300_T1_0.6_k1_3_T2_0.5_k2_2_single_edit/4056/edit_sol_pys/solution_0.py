

def Gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def main():
    n = int(input())
    a = list(map(int, input().split()))

divisors = []

for i in range(1, int(sqrt(gcd)) + 1):
    if gcd % i == 0:
        divisors.append(i)
        if i != gcd // i:
            divisors.append(gcd // i)

print(len(divisors))
