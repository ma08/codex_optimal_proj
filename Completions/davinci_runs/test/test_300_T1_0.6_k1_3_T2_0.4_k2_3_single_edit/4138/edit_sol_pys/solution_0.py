

def get_digit(num):
    if num == 1:
        return 1
    else:
        # get the number of digits.
        digits = 1
        num -= 1
        while (10**digits - 1) // 9 < num: # number of digits in the range [1, 10**digits-1]
            num -= (10**digits-1) // 9 # number of digits in the range [1, 10**(digits-1)-1]
            digits += 1
        
        # get the actual number.
        num_str = str(num-1) # num is the index of the number, so it's num-1.
        if len(num_str) < digits:
            num_str = '0'*(digits-len(num_str)) + num_str
        return int(num_str[digits-1])

q = int(input())
for _ in range(q):
    print(get_digit(int(input())))
