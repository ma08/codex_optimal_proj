

# Solution

def get_digit(k):
    if k == 1:
        return 1
    sum_digits = 9
    digits = 1
    while True:
        sum_digits = sum_digits + (9 * digits * 10**(digits-1))
        if k <= sum_digits:
            break
        digits += 1
    # print(digits)
    num = 10**(digits-1)
    # print(num)
    number_of_digits = sum_digits - k + 1
    # print(number_of_digits)
    if number_of_digits % digits == 0:
        number_of_digits = digits
        num -= 1
    else:
        number_of_digits = number_of_digits % digits
    # print(number_of_digits)
    # print(num)
    num = str(num)
    return num[number_of_digits-1]

q = int(input())
for _ in range(q):
    k = int(input())
    print(int(get_digit(k)))