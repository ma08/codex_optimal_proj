

#Solved by Shashwat Raj

def sum_of_digits(n):
    sum = 0
    while n > 0:
        sum += n % 10
        n = int(n / 10)
    return sum

a = int(input())

while sum_of_digits(a) % 4 != 0:
    a += 1

print(a)