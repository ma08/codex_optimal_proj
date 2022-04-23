
# n, k = map(int, input().split())
# a = list(map(int, input().split()))

# def concat(x, y):
#     return (x * 10**len(str(y))) + y

# def count_divisible(x):
#     count = 0
#     for i in range(n):
#         if concat(x, a[i]) % k == 0:
#             count += 1
#     return count

# total = 0
# for i in range(n):
#     total += count_divisible(a[i])

# print(total)


n = int(input())
a = list(map(int, input().split()))

def is_prime(n):
    if n == 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

def count_prime(n):
    count = 0
    for i in range(n):
        if is_prime(a[i]):
            count += 1
    return count

print(count_prime(n))
