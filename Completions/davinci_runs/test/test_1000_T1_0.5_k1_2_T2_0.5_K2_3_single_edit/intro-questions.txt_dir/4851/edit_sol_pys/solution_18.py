
n = int(input())

while True:
    sum_of_digits = sum([int(digit) for digit in list(str(n))])
    if n % sum_of_digits == 0:
        print(n)
        break
    else:
        n += 1
