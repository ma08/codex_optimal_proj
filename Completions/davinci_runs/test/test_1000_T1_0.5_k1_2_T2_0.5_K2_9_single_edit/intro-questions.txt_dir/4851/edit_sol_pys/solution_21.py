
#function to find sum of digits
n = int(input())

def sum_digits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s
#loop to find the smallest number that is divisible by the sum of its digits
while n % sum_digits(n) != 0:
    n += 1
print(n)
