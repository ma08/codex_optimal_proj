

n = int(input())
a = list(map(int, input().split()))

# 1. 約数を列挙する
def divisor(n):
    divisors = []
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            divisors.append(i)
            if i != n // i:
                divisors.append(n//i)

    # divisors.sort(reverse=True)  # ソート
    return divisors

a_divisors = [divisor(a_i) for a_i in a]

# 2. 共通約数を探す
def common_divisor(a, b):
    c = []
    for a_i in a:
        if a_i in b:
            c.append(a_i)
    return c

common_divisors = []
for i in range(len(a_divisors)):
    if i == 0:
        common_divisors = a_divisors[i]
    else:
        common_divisors = common_divisor(common_divisors, a_divisors[i])

print(max(common_divisors))