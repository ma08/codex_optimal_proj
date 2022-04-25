
def max_divisor(n):
    div = 1
    for i in range(1, n):
        if n % i == 0:
            div = i
    return div

n = int(input())

print(max_divisor(n))
