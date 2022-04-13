import itertools, math

def get_divisors(n):
    divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            if n / i == i:
                divisors.append(i)
            else:
                divisors.append(i)
                divisors.append(int(n / i))
    return divisors

def get_divisors_sum(n):
    return sum(get_divisors(n))

n = int(input())
divisors = get_divisors(n)
divisors_sum = get_divisors_sum(n)
if divisors_sum == n:
    print('perfect')
elif divisors_sum < n:
    print('deficient')
else:
    print('abundant')
