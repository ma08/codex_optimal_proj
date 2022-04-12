

def check_harshad_number(n):
    s_n = str(n)
    s_sum = sum([int(i) for i in s_n])
    if n % s_sum == 0: 
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(check_harshad_number(int(input())))
