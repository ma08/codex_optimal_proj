
def find_sum(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n //= 10
    return sum
    
n = 123
print(find_sum(n))
