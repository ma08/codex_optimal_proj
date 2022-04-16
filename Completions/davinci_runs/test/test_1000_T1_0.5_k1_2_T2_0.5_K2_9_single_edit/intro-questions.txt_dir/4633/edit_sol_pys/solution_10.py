

# def sumOfDigits(n):
#     sum = 0
#     for i in n:
#         sum += int(i)
#     return sum

# def getMinMoves(n):
#     n = str(n)
#     nSum = sumOfDigits(n)
#     if nSum <= s:
#         return 0
#     else:
#         moves = 0
#         i = 0
#         while nSum > s:
#             if i == len(n) - 1:
#                 n = str(int(n) + 1)
#                 i = 0
#                 moves += 1
#             else:
#                 n = n[:i] + str(int(n[i]) - 1) + n[i+1:]
#                 i += 1
#             nSum = sumOfDigits(n)
#         return moves

# t = int(input())

# for i in range(t):
#     n, s = map(int, input().split())
#     print(getMinMoves(n))

# def getLcm(a, b):
#     i = 2
#     while i <= min(a,b):
#         if a % i == 0 and b % i == 0:
#             return i
#         i += 1
#     return 1

# def getGcd(a,b):
#     while b:
#         a, b = b, a % b
#     return a

# t = int(input())

# for i in range(t):
#     a, b = map(int, input().split())
#     lcm = getLcm(a, b)
#     gcd = getGcd(a, b)
#     print(lcm * gcd)

def getFactors(n):
    factors = []
    for i in range(1, n + 1):
        if n % i == 0:
            factors.append(i)
    return factors

t = int(input())

for i in range(t):
    n = int(input())
    factors = getFactors(n)
    print(len(factors))
