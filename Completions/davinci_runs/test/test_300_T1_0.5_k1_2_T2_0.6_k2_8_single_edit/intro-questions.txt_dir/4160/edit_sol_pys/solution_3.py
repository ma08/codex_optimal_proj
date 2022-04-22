

n = int(input())

def count_digit(n):
    if n < 10:
        return 1
    else:
        return 1 + count_digit(n // 10)

print(count_digit(n))
