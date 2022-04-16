
n = int(input())

sum_of_digits = sum([int(d) for d in list(str(n))])
if n % sum_of_digits == 0:
    print(n)
else:
    n += 1
