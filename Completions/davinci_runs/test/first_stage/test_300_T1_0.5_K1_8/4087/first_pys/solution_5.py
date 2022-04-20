

def is_interesting(number):
    sum_of_digits = 0
    for digit in number:
        sum_of_digits += int(digit)
    return sum_of_digits % 4 == 0

n = int(input())
while True:
    if is_interesting(str(n)):
        print(n)
        break
    else:
        n += 1