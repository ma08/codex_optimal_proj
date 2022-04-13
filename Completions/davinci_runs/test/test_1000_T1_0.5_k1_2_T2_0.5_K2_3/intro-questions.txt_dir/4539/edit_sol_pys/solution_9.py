

def check_harshad(n):
    s_n = str(n)
    s_sum = sum([int(x) for x in s_n])
    if n % s_sum == 0:
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':
    print(check_harshad(int(input())))
