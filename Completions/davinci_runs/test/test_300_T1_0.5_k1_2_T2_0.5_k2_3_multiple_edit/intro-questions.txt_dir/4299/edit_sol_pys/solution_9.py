
n = int(input())
one_digit = n % 10
if one_digit == 2 or one_digit == 4 or one_digit == 5 or one_digit == 7 or one_digit == 9:
    print("hon")
elif one_digit == 0 or one_digit == 1 or one_digit == 6 or one_digit == 8:
    print("pon")
elif one_digit == 3:
    print("bon")
