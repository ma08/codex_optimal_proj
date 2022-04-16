

n = int(input())

while True:
    sum_of_digits = sum([int(d) for d in str(n)])
    if n % sum_of_digits == 0 or n == sum_of_digits:
        print(n)
        break
    else:
        n += 1
