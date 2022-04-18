def sum_digits(n):
    """
    Return the sum of digits of n
    """
    s = 0
    for i in str(n):
        s += int(i)
    return s

n = int(input("Enter a number: "))

while n % sum_digits(n) != 0:


    n += 1
print(n)
