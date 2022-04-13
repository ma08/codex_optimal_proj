def sum_of_digits(n):
    return sum([int(i) for i in str(n)])

n, a, b = map(int, input().split())

res = 0
for i in range(1, n+1):
    if a <= sum_of_digits(i) <= b:
        res += i

print(res)
