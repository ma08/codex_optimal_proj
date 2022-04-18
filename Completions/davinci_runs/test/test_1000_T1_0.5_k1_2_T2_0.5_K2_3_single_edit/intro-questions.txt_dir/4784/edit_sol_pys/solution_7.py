

def sum_of_digits(n):
    sum = 0
    for i in str(n):
        sum += int(i)
    return sum


x = int(input("Enter a number: "))
print("Sum of digits: ", sum_of_digits(x))
