def is_nine(n):
    if n % 9 == 0:
        return "Yes"
    else:
        return "No"



n = int(input())  # input number
print(is_nine(n))  # output result
