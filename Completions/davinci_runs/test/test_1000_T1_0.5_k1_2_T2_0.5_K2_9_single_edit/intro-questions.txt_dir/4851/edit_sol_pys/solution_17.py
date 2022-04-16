import sys

n = int(sys.stdin.readline().strip())

def generate_next_self_describing_number(n):
    while True:
        n += 1
        sum_digits = 0
        for digit in str(n):
            sum_digits += int(digit)
        if n % sum_digits == 0:
            break

    print(n)

generate_next_self_describing_number(n)
