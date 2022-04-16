
def check_harshad(n):
    str_n = str(n)
    sum_of_digits = sum([int(x) for x in str_n])
    if n % sum_of_digits == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(check_harshad(int(input())))
