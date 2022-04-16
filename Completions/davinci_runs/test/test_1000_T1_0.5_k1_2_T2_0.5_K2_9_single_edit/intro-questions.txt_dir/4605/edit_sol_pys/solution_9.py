

a, b = map(int, input().split())

def sum_of_digits(x):
    return sum([int(i) for i in str(x)])

res = 0
for i in range(1, 10000):
    if a <= sum_of_digits(i) <= b:
        res += i

print(res)
