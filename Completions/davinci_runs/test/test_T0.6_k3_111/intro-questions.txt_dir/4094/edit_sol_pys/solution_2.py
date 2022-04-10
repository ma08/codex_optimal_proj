

def get_num_digits(num):
    return len(str(num)) 
# end get_num_digits

def get_first_multiple_of_7(k):
    if k % 7 == 0:
        return 1
    else:
        digits = 1
        while True:
            num = 7*10**(digits-1)
            if num % k == 0:
                break
            else:
                digits += 1
        return digits
    # end if
# end get_first_multiple_of_7

k = int(input())
print(get_first_multiple_of_7(k))
